from django.contrib import admin
from .models import *

# Oddiy modellar uchun umumiy admin klassi
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


# UserModelInfo uchun admin sozlamalari
class UserModelInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'tashkilot', 'hudud', 'data', 'natija']
    list_filter = ['tashkilot', 'hudud', 'jinoyat', 'natija']
    search_fields = ['name', 'number', 'manzil', 'holat_mazmuni']
    date_hierarchy = 'data'
    readonly_fields = ['karta_number',]  # Shifrlangan maydonlar faqat o'qish uchun
    fieldsets = (
        (None, {
            'fields': ('data', 'number', 'name', 'manzil', 'tell')
        }),
        ('Tashkilot va Hudud', {
            'fields': ('tashkilot', 'hudud')
        }),
        ('Jinoyat tafsilotlari', {
            'fields': ('jinoyat', 'holat_mazmuni', 'xitr', 'ilova')
        }),
        ('Moliyaviy tafsilotlar', {
            'fields': ('bank', 'karta_number', 'zarar',)
        }),
        ('Natija', {
            'fields': ('natija',)
        }),
    )


@admin.register(CategoryAJ)
class CategoryAJAdmin(admin.ModelAdmin):
    list_display = ['title', 'sup']
    search_fields = ['title']


@admin.register(AJ_article)
class CategoryAJAdmin(admin.ModelAdmin):
    list_display = ['hudud', 'data']
    search_fields = ['hudud']


@admin.register(Article_Boshqa_tashkilot)
class Article_Boshqa_tashkilotAdmin(admin.ModelAdmin):
    list_display = ['hudud', 'data']
    search_fields = ['hudud']





@admin.register(Article_FJ)
class Article_FJAdmin(admin.ModelAdmin):
    list_display = ['hudud', 'data']
    search_fields = ['hudud']



@admin.register(TargibotBoshqa)
class TargibotBoshqaAdmin(admin.ModelAdmin):
    list_display = ['title', 'hudud']
    search_fields = ['title', 'hudud']



@admin.register(TargibotBulim)
class TargibotBulimAdmin(admin.ModelAdmin):
    list_display = ['title', 'hudud']
    search_fields = ['title', 'hudud']



admin.site.register(BankModel, BaseModelAdmin)
admin.site.register(TashkilotModel, BaseModelAdmin)
admin.site.register(HududModel, BaseModelAdmin)
admin.site.register(JinoyatModel, BaseModelAdmin)
admin.site.register(IlovaModel, BaseModelAdmin)
admin.site.register(XitrModel, BaseModelAdmin)
admin.site.register(ResultModel, BaseModelAdmin)
admin.site.register(JobsModel)
admin.site.register(UserModelInfo, UserModelInfoAdmin)