from django.shortcuts import render, redirect, get_object_or_404
import pandas as pd
from django.utils import timezone
from django.views import View
from django.contrib.auth import authenticate, login
from myapp.forms import UserModelInfoForm
from django.contrib import messages
from django.http import HttpResponse, Http404
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myapp.models import *
from myapp.forms import *
from django.http import HttpResponseBadRequest
import logging



logger = logging.getLogger(__name__)


class IndexView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)





# Ma'lumot yaratish uchun view
class CreateView(View):
    template_name = 'create.html'

    def prepare_context(self, form=None):
        """Kontekst ma'lumotlarini tayyorlash."""
        return {
            'form': form or UserModelInfoForm(),
            'banklar': BankModel.objects.all(),
            'tashkilotlar': TashkilotModel.objects.all(),
            'hududlar': HududModel.objects.all(),
            'jinoyatlar': JinoyatModel.objects.all(),
            'ilovalar': IlovaModel.objects.all(),
            'xitrlar': XitrModel.objects.all(),
            'natijalar': ResultModel.objects.all(),
        }

    def get(self, request):
        context = self.prepare_context()
        logger.debug("GET so'rovi: Tashkilotlar ro'yxati - %s", context['tashkilotlar'])
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserModelInfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                logger.info("Ma'lumot muvaffaqiyatli saqlandi: %s", form.cleaned_data.get('number'))
                messages.success(request, "Ma'lumot muvaffaqiyatli saqlandi!")
                return redirect('table')
            except Exception as e:
                logger.error("Ma'lumotni saqlashda xatolik: %s", str(e))
                messages.error(request, f"Ma'lumotni saqlashda xatolik yuz berdi: {str(e)}")
        else:
            logger.warning("Forma xatolari: %s", form.errors.as_text())
            messages.error(request, "Forma xato to‘ldirilgan. Iltimos, quyidagi xatolarni tuzating.")

        context = self.prepare_context(form)
        return render(request, self.template_name, context)










class TableView(View):
    template_name = 'table.html'
    paginate_by = 25  # Har sahifada 25 ta yozuv

    def get(self, request):
        # Eksport so'rovi
        if 'export' in request.GET and request.GET['export'] == 'excel':
            data = UserModelInfo.objects.select_related(
                'tashkilot', 'hudud', 'jinoyat', 'bank', 'ilova', 'xitr', 'natija','jobs'
            ).all()
            raw_data = list(data.values(
                'id', 'data', 
                'tashkilot__title', 'hudud__title', 'number', 'name', 'manzil', 'tell',
                'holat_mazmuni', 'jinoyat__title', 'karta_number', 'bank__title', 
                'ilova__title', 'xitr__title', 'zarar', 'natija__title','jobs__title', 'files',
                
            ))
            for item in raw_data:
                if item['data'] and timezone.is_aware(item['data']):
                    item['data'] = timezone.make_naive(item['data'])
            df = pd.DataFrame(raw_data)
            df.columns = [
                'ID', 'Sana', 'Tashkilot', 'Hudud', 'FISH', 'Kasbi', 'Hudud', 'Tell',
                'Holat mazmuni', 'Murojaat turi', 'Bank kartasi', 'Bank nomi', 'Mobil ilova', 
                'Sodir etish usuli', 'Zarar', 'Natija','files'
            ]
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            current_date = datetime.now().strftime('%Y-%m-%d')
            response['Content-Disposition'] = f'attachment; filename="malumotlar_{current_date}.xlsx"'
            df.to_excel(response, index=False, engine='openpyxl')
            logger.info("Ma'lumotlar Excel sifatida yuklab olindi: %s", current_date)
            return response

        # Filtrlash logikasi
        data = UserModelInfo.objects.select_related(
            'tashkilot', 'hudud', 'jinoyat', 'bank', 'ilova', 'xitr', 'jobs'
        ).all()

        # Filtrlar
        jinoyat_filter = request.GET.get('jinoyat')
        hudud_filter = request.GET.get('hudud')
        bank_filter = request.GET.get('bank')
        jobs_filter = request.GET.get('jobs')
        ilova_filter = request.GET.get('ilova')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if jinoyat_filter:
            data = data.filter(jinoyat__title=jinoyat_filter)
        if hudud_filter:
            data = data.filter(hudud__filter=hudud_filter)
        if jobs_filter:
            data = data.filter(jobs__title=jobs_filter)
        if bank_filter:
            data = data.filter(bank__title=bank_filter)
        if ilova_filter:
            data = data.filter(ilova__title=ilova_filter)
        if start_date:
            try:
                start = datetime.strptime(start_date, '%Y-%m-%d')
                data = data.filter(data__gte=start)
            except ValueError:
                logger.warning("Noto'g'ri boshlang'ich sana formati: %s", start_date)
                messages.error(request, "Noto‘g‘ri boshlang‘ich sana formati kiritildi.")
        if end_date:
            try:
                end = datetime.strptime(end_date, '%Y-%m-%d')
                data = data.filter(data__lte=end)
            except ValueError:
                logger.warning("Noto'g'ri tugash sana formati: %s", end_date)
                messages.error(request, "Noto‘g‘ri tugash sana formati kiritildi.")

        # Paginatsiya
        paginator = Paginator(data.order_by('-data'), self.paginate_by)
        # Faqat oxirgi 'page' parametrini olish
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'data': page_obj,
            'jinoyats': JinoyatModel.objects.all(),
            'banks': BankModel.objects.all(),
            'ilovas': IlovaModel.objects.all(),
            'Hududs': HududModel.objects.all(),
            'jobs': JobsModel.objects.all(),
        }
        logger.debug("Ro'yxat so'rovi: Jami ma'lumotlar soni - %d, Sahifa - %s", data.count(), page_number or 1)
        return render(request, self.template_name, context)






# Ma'lumotni tahrirlash uchun view
class UpdateView(View):
    template_name = 'update.html'

    def prepare_context(self, form=None):
        """Kontekst ma'lumotlarini tayyorlash."""
        return {
            'form': form or UserModelInfoForm(),
            'banklar': BankModel.objects.all(),
            'tashkilotlar': TashkilotModel.objects.all(),
            'hududlar': HududModel.objects.all(),
            'jinoyatlar': JinoyatModel.objects.all(),
            'ilovalar': IlovaModel.objects.all(),
            'xitrlar': XitrModel.objects.all(),
            'natijalar': ResultModel.objects.all(),
        }

    def get(self, request, pk):
        user_info = get_object_or_404(UserModelInfo, pk=pk)
        form = UserModelInfoForm(instance=user_info)
        context = self.prepare_context(form)
        logger.debug("Tahrirlash so'rovi: F2-raqam %s", user_info.number)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        user_info = get_object_or_404(UserModelInfo, pk=pk)
        form = UserModelInfoForm(request.POST, instance=user_info)
        if form.is_valid():
            try:
                form.save()
                logger.info("Ma'lumot muvaffaqiyatli yangilandi: F2-raqam %s", form.cleaned_data.get('number'))
                messages.success(request, "Ma'lumot muvaffaqiyatli yangilandi!")
                return redirect('table')
            except Exception as e:
                logger.error("Ma'lumotni yangilashda xatolik: %s", str(e))
                messages.error(request, f"Ma'lumotni yangilashda xatolik yuz berdi: {str(e)}")
        else:
            logger.warning("Forma xatolari: %s", form.errors.as_text())
            messages.error(request, "Forma xato to‘ldirilgan. Iltimos, quyidagi xatolarni tuzating.")

        context = self.prepare_context(form)
        return render(request, self.template_name, context)


# Ma'lumotni o'chirish uchun view
class DeleteView(View):
    def post(self, request, pk):
        user_info = get_object_or_404(UserModelInfo, pk=pk)
        try:
            number = user_info.number
            user_info.delete()
            logger.info("Ma'lumot muvaffaqiyatli o'chirildi: F2-raqam %s", number)
            messages.success(request, "Ma'lumot muvaffaqiyatli o'chirildi!")
        except Exception as e:
            logger.error("Ma'lumotni o'chirishda xatolik: %s", str(e))
            messages.error(request, f"Ma'lumotni o'chirishda xatolik yuz berdi: {str(e)}")
        return redirect('table')
    




########################################
##                                    ##
##    Login views                     ##
##                                    ##
########################################

class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:index")
        else:
            return render(request, self.template_name, {"error": "Foydalanuvchi nomi yoki parol noto‘g‘ri!"})



########################################
##                                    ##
##    Aniqlangan Jinoyatlar views     ##
##                                    ##
########################################


class JinoyatAllView(View):
    template_name = 'jinoyat/AJ/aniqlangan-jinoyatlar.html'
    paginate_by = 10

    def get(self, request, id=None):
        # Formani bo'sh holatda tayyorlash (filtr uchun)
        form = AJ_articleForm()

        # Filtrlash uchun so'rovdan qiymatlarni olish
        category_filter = request.GET.get('category', '')
        hudud_filter = request.GET.get('hudud', '')
        data_filter = request.GET.get('data', '')

        # Boshlang'ich queryset
        articles = AJ_article.objects.all()

        # Filtrlash
        if category_filter:
            articles = articles.filter(category__id=category_filter)  # `id` bo'yicha filtr
        if hudud_filter:
            articles = articles.filter(hudud__id=hudud_filter)  # `id` bo'yicha filtr
        if data_filter:
            articles = articles.filter(data=data_filter)  # Faqat sana bo'yicha filtr

        # Pagination
        paginator = Paginator(articles, self.paginate_by)
        page = request.GET.get('page') or 1

        try:
            paginated_articles = paginator.page(page)
        except PageNotAnInteger:
            paginated_articles = paginator.page(1)
        except EmptyPage:
            paginated_articles = paginator.page(paginator.num_pages)

        # Kategoriya va hududlar ro'yxatini olish
        categories = CategoryAJ.objects.all()
        hududs = HududModel.objects.all()

        context = {
            'form': form,
            'article': paginated_articles,
            'category_filter': category_filter,
            'hudud_filter': hudud_filter,
            'data_filter': data_filter,
            'categories': categories,
            'hududs': hududs,
        }

        return render(request, self.template_name, context)
    


class CreateArticleView(View):
    template_name = 'jinoyat/AJ/create_jinoyat.html'

    def get(self, request):
        form = AJ_articleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AJ_articleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:jinoyat_list')
        return render(request, self.template_name, {'form': form})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Faqat GET va POST so'rovlari qo'llab-quvvatlanadi.")
    
    
    
    
    
########################################
##                                    ##
##    Fosh-elitgan Jinoyatlar views   ##
##                                    ##
########################################



class JinoyatAll_FEJ_View(View):
    template_name = 'jinoyat/FEJ/fosh-etilgan-jinoyat.html'
    paginate_by = 10

    def get(self, request, id=None):
        # Formani bo'sh holatda tayyorlash (filtr uchun)
        form = Article_FJForm()  # GET so'rovida POST ishlatilmaydi

        # Filtrlash uchun so'rovdan qiymatlarni olish
        category_filter = request.GET.get('category', '')
        hudud_filter = request.GET.get('hudud', '')
        data_filter = request.GET.get('data', '')

        # Boshlang'ich queryset
        articles = Article_FJ.objects.all()

        # Filtrlash
        if category_filter:
            articles = articles.filter(category__id=category_filter)  # ForeignKey uchun id
        if hudud_filter:
            articles = articles.filter(hudud__id=hudud_filter)  # ForeignKey uchun id
        if data_filter:
            articles = articles.filter(data=data_filter)  # Faqat sana bo'yicha filtr

        # Pagination
        paginator = Paginator(articles, self.paginate_by)
        page = request.GET.get('page') or 1

        try:
            paginated_articles = paginator.page(page)
        except PageNotAnInteger:
            paginated_articles = paginator.page(1)
        except EmptyPage:
            paginated_articles = paginator.page(paginator.num_pages)

        # Kategoriya va hududlar ro'yxatini olish (select uchun)
        categories = CategoryAJ.objects.all()
        hududs = HududModel.objects.all()

        context = {
            'form': form,
            'article': paginated_articles,
            'category_filter': category_filter,
            'hudud_filter': hudud_filter,
            'data_filter': data_filter,
            'categories': categories,
            'hududs': hududs,
        }

        return render(request, self.template_name, context)

class CreateArticle_FEJ_View(View):
    template_name = 'jinoyat/FEJ/fosh-etilgan-jinoyat-create.html'

    def get(self, request):
        form = Article_FJForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Article_FJForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:FEJ_list')
        return render(request, self.template_name, {'form': form})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Faqat GET va POST so'rovlari qo'llab-quvvatlanadi.")
    
    
    

########################################
##                                    ##
##    Boshqa Xizmatlar tomonidan      ##
##    Aniqlangan va Fosh-etilgan      ##
##    Jinoyatlar views                ##
##                                    ##
########################################


class Boshqa_tashkilot_View(View):
    template_name = 'jinoyat/BTJ/boshqa.html'
    paginate_by = 10

    def get(self, request, id=None):
        # Formani bo'sh holatda tayyorlash (filtr uchun)
        form = Article_Boshqa_tashkilotForm()  # GET so'rovida POST ishlatilmaydi

        # Filtrlash uchun so'rovdan qiymatlarni olish
        category_filter = request.GET.get('category', '')
        hudud_filter = request.GET.get('hudud', '')
        data_filter = request.GET.get('data', '')

        # Boshlang'ich queryset
        articles = Article_Boshqa_tashkilot.objects.all()

        # Filtrlash
        if category_filter:
            articles = articles.filter(category__id=category_filter)  # ForeignKey uchun id
        if hudud_filter:
            articles = articles.filter(hudud__id=hudud_filter)  # ForeignKey uchun id
        if data_filter:
            articles = articles.filter(data=data_filter)  # Faqat sana bo'yicha filtr


        # Pagination
        paginator = Paginator(articles, self.paginate_by)
        page = request.GET.get('page') or 1

        try:
            paginated_articles = paginator.page(page)
        except PageNotAnInteger:
            paginated_articles = paginator.page(1)
        except EmptyPage:
            paginated_articles = paginator.page(paginator.num_pages)

        # Kategoriya va hududlar ro'yxatini olish (select uchun)
        categories = CategoryAJ.objects.all()
        hududs = HududModel.objects.all()

        context = {
            'form': form,
            'article': paginated_articles,
            'category_filter': category_filter,
            'hudud_filter': hudud_filter,
            'data_filter': data_filter,
            'categories': categories,
            'hududs': hududs,
        }

        return render(request, self.template_name, context)

class Boshqa_tashkilot_Create_View(View):
    template_name = 'jinoyat/BTJ/boshqa_create.html'

    def get(self, request):
        form = Article_Boshqa_tashkilotForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Article_Boshqa_tashkilotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:BTJ_list')
        return render(request, self.template_name, {'form': form})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Faqat GET va POST so'rovlari qo'llab-quvvatlanadi.")
    
    
    

########################################
##                                    ##
##    Bo'lim Targ'iboti               ##
##                                    ##
########################################


class targibot_bulim_View(View):
    template_name = 'targibot/bulim/bulim.html'
    paginate_by = 10

    def get(self, request, id=None):
        form = TargibotBulimForm()

        # Boshlang'ich queryset
        articles = TargibotBulim.objects.all()

        # Pagination
        paginator = Paginator(articles, self.paginate_by)
        page = request.GET.get('page') or 1

        try:
            paginated_articles = paginator.page(page)
        except PageNotAnInteger:
            paginated_articles = paginator.page(1)
        except EmptyPage:
            paginated_articles = paginator.page(paginator.num_pages)
            
        targibot = TargibotBulim.objects.all()

        context = {
            'form': form,
            'article': paginated_articles,
            'targibot': targibot,
        }

        return render(request, self.template_name, context)
    
    
class targibot_bulim_Create_View(View):
    template_name = 'targibot/bulim/create.html'

    def get(self, request):
        form = TargibotBulimForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TargibotBulimForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:targibot-bulim_list')
        return render(request, self.template_name, {'form': form})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Faqat GET va POST so'rovlari qo'llab-quvvatlanadi.")






########################################
##                                    ##
##    Targ'ibot                       ##
##    boshqa tashkilot tomonidan      ##
##                                    ##
########################################


class targibot_boshqa_View(View):
    template_name = 'targibot/boshqa/boshqa.html'
    paginate_by = 10

    def get(self, request, id=None):
        form = TargibotBoshqaForm()

        # Boshlang'ich queryset
        articles = TargibotBoshqa.objects.all()

        # Pagination
        paginator = Paginator(articles, self.paginate_by)
        page = request.GET.get('page') or 1

        try:
            paginated_articles = paginator.page(page)
        except PageNotAnInteger:
            paginated_articles = paginator.page(1)
        except EmptyPage:
            paginated_articles = paginator.page(paginator.num_pages)
            
        targibot = TargibotBoshqa.objects.all()

        context = {
            'form': form,
            'article': paginated_articles,
            'targibot': targibot,
        }

        return render(request, self.template_name, context)
    
    
class targibot_boshqa_Create_View(View):
    template_name = 'targibot/boshqa/create.html'

    def get(self, request):
        form = TargibotBoshqaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TargibotBoshqaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:targibot-boshqa_list')
        return render(request, self.template_name, {'form': form})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseBadRequest("Faqat GET va POST so'rovlari qo'llab-quvvatlanadi.")