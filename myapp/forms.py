from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator
from fernet_fields import EncryptedCharField
from datetime import date, datetime
from django.utils import timezone


# Umumiy forma uchun abstrakt sinf
class CategoryAJForm(forms.ModelForm):
    class Meta:
        model = CategoryAJ
        fields = ['title', 'sup']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'modda raqami',
                'class': 'form-control'
            }),
            'sup': forms.TextInput(attrs={
                'placeholder': 'modda raqami',
                'class': 'form-control'
            }),
        }





class AJ_articleForm(forms.ModelForm):
    class Meta:
        model = AJ_article
        fields = ['category', 'hudud', 'data', 'files']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'hudud': forms.Select(attrs={'class': 'selects form-control'}),
            'data': forms.DateTimeInput(attrs={'placeholder': 'Sana (YYYY-MM-DD HH:MM)', 'class': 'form-control', 'type': 'date'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'category': 'Kategoriya',
            'hudud': 'Hudud',
            'data': 'Sana',
            'files': 'Fayllar',
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if isinstance(data, datetime):
            data_date = data.date()
            current_date = date.today()
            if data_date > current_date:
                raise forms.ValidationError("Sana kelajakda bo‘lishi mumkin emas.")
        elif isinstance(data, date):
            if data > date.today():
                raise forms.ValidationError("Sana kelajakda bo‘lishi mumkin emas.")
        return data



class Article_Boshqa_tashkilotForm(forms.ModelForm):
    class Meta:
        model = Article_Boshqa_tashkilot
        fields = ['category', 'hudud', 'data', 'files']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'hudud': forms.Select(attrs={'class': 'selects form-control'}),
            'data': forms.DateTimeInput(attrs={'placeholder': 'Sana (YYYY-MM-DD HH:MM)', 'class': 'form-control', 'type': 'date'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'category': 'Kategoriya',
            'hudud': 'Hudud',
            'data': 'Sana',
            'files': 'Fayllar',
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if isinstance(data, datetime):
            data_date = data.date()
            current_date = date.today()
            if data_date > current_date:
                raise forms.ValidationError("Sana kelajakda bo‘lishi mumkin emas.")
        elif isinstance(data, date):
            if data > date.today():
                raise forms.ValidationError("Sana kelajakda bo‘lishi mumkin emas.")
        return data










class Article_FJForm(forms.ModelForm):
    class Meta:
        model = Article_FJ
        fields = ['category', 'hudud', 'data', 'files']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'hudud': forms.Select(attrs={'class': 'selects form-control'}),
            'data': forms.DateTimeInput(attrs={'placeholder': 'Sana (YYYY-MM-DD HH:MM)', 'class': 'form-control', 'type': 'date'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'category': 'Kategoriya',
            'hudud': 'Hudud',
            'data': 'Sana',
            'files': 'Fayllar',
        }

    def clean_data(self):
        data = self.cleaned_data['data']
        if isinstance(data, datetime):
            data_date = data.date()
            current_date = date.today()
            if data_date > current_date:
                raise forms.ValidationError("Sana kelajakda bo‘lishi mumkin emas.")
        elif isinstance(data, date):
            if data > date.today():
                raise forms.ValidationError("Sana kelajakda bo‘lishi mumkin emas.")
        return data


















class BaseModelForm(forms.ModelForm):
    class Meta:
        abstract = True
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Nomi bo'sh bo'lmasligi kerak")
        return title.strip()


# BankModel uchun forma
class BankModelForm(BaseModelForm):
    class Meta:
        model = BankModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Bank nomini kiriting',
                'class': 'form-control'
            }),
        }


# TashkilotModel uchun forma
class TashkilotModelForm(BaseModelForm):
    class Meta:
        model = TashkilotModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Tashkilot nomini kiriting',
                'class': 'form-control'
            }),
        }


# HududModel uchun forma
class HududModelForm(BaseModelForm):
    class Meta:
        model = HududModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Hudud nomini kiriting',
                'class': 'form-control'
            }),
        }


# JinoyatModel uchun forma
class JinoyatModelForm(BaseModelForm):
    class Meta:
        model = JinoyatModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Jinoyat turini kiriting',
                'class': 'form-control'
            }),
        }


# IlovaModel uchun forma
class IlovaModelForm(BaseModelForm):
    class Meta:
        model = IlovaModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Ilova nomini kiriting',
                'class': 'form-control'
            }),
        }


# XitrModel uchun forma
class XitrModelForm(BaseModelForm):
    class Meta:
        model = XitrModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Sodir etish usulini kiriting',
                'class': 'form-control'
            }),
        }


# ResultModel uchun forma
class ResultModelForm(BaseModelForm):
    class Meta:
        model = ResultModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Natija holatini kiriting',
                'class': 'form-control'
            }),
        }


# JobsModel uchun forma
class JobsModelForm(BaseModelForm):
    class Meta:
        model = JobsModel
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Natija holatini kiriting',
                'class': 'form-control'
            }),
        }





class UserModelInfoForm(forms.ModelForm):
    # Telefon raqami uchun maxsus maydon
    tell = PhoneNumberField(
        required=False,
        label="Telefon raqami",
        help_text="Masalan: +998901234567"
    )

    # Karta raqami uchun maxsus validatsiya
    karta_number = forms.CharField(
        max_length=16,
        required=False,
        label="Bank Karta raqami",
        validators=[RegexValidator(regex=r'^\d{16}$', message="Karta raqami 16 raqamdan iborat bo‘lishi kerak")],
        help_text="16 raqamli karta raqamini kiriting"
    )

    class Meta:
        model = UserModelInfo
        fields = [
            'data', 'tashkilot', 'hudud', 'number', 'name', 'manzil', 'tell',
            'holat_mazmuni', 'jinoyat', 'karta_number', 'bank', 'ilova', 'xitr',
            'zarar', 'natija', 'pul_data', 'files','jobs'
        ]
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'tashkilot': forms.Select(attrs={'class': 'selects'}),
            'hudud': forms.Select(attrs={'class': 'selects'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Murojaat Muallifini shaxsi'}),
            'manzil': forms.TextInput(attrs={'class': 'selects', 'placeholder': 'Manzil'}),
            'holat_mazmuni': forms.Textarea(attrs={'class': 'text-area', 'rows': 4, 'placeholder': 'Holat mazmuni'}),
            'jinoyat': forms.Select(attrs={'class': 'selects'}),
            'karta_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234567890123456'}),
            'bank': forms.Select(attrs={'class': 'selects'}),
            'ilova': forms.Select(attrs={'class': 'selects'}),
            'jobs': forms.Select(attrs={'class': 'selects'}),
            'xitr': forms.Select(attrs={'class': 'selects'}),
            'zarar': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.00001'}),
            'natija': forms.Select(attrs={'class': 'selects'}),
            'pul_data': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'files': forms.ClearableFileInput(attrs={'class': 'form-control', 'id':'files'}),  # files uchun widget
        }
        labels = {
            'data': 'Murojaat tushgan sana',
            'tashkilot': 'Tashkilot',
            'hudud': 'Hudud',
            'number': 'Raqam',
            'name': 'F.I.SH',
            'manzil': 'Manzil',
            'tell': 'Telefon raqami',
            'holat_mazmuni': 'Holat mazmuni',
            'jinoyat': 'Murojaat turi',
            'karta_number': 'Bank Karta raqami',
            'bank': 'Bank',
            'ilova': 'Ilova',
            'jobs': 'Kabingizni kiriting',
            'xitr': 'Sodir etish usuli',
            'zarar': 'Zarar miqdori',
            'natija': 'Natija holati',
            'pul_data': 'Pul o‘tkazma sanasi',
            'files': 'Fayllar',  # files uchun label
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agar forma tahrirlanayotgan bo‘lsa, karta_number ni to‘g‘ri ko‘rsatish
        if self.instance and self.instance.pk and self.instance.karta_number:
            self.fields['karta_number'].initial = self.instance.karta_number

    def clean_karta_number(self):
        karta_number = self.cleaned_data.get('karta_number')
        if karta_number:
            if not len(karta_number) == 16 or not karta_number.isdigit():
                raise forms.ValidationError("Karta raqami 16 raqamdan iborat bo‘lishi kerak.")
        return karta_number

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data and data > timezone.now():
            raise forms.ValidationError("Sana kelajakda bo‘lishi mumkin emas.")
        return data

    def clean_pul_data(self):
        pul_data = self.cleaned_data.get('pul_data')
        if pul_data and pul_data > timezone.now():
            raise forms.ValidationError("Pul o‘tkazma sanasi kelajakda bo‘lishi mumkin emas.")
        return pul_data

    def clean_zarar(self):
        zarar = self.cleaned_data.get('zarar')
        if zarar and zarar < 0:
            raise forms.ValidationError("Zarar miqdori manfiy bo‘lishi mumkin emas.")
        return zarar

    def clean_files(self):
        files = self.cleaned_data.get('files')
        if files:
            # Fayl hajmini tekshirish (masalan, 100MB dan katta bo‘lmasligi uchun)
            if files.size > 100 * 1024 * 1024:  # 100MB limit
                raise forms.ValidationError("Fayl hajmi 5MB dan katta bo‘lmasligi kerak.")
            # Fayl turini tekshirish (masalan, faqat PDF, rasm va hokazo)
            allowed_types = ['application/pdf', 'image/jpeg', 'image/png']
            if files.content_type not in allowed_types:
                raise forms.ValidationError("Faqat PDF, JPEG yoki PNG fayllarni yuklash mumkin.")
        return files
    
    
    
    
class TargibotBulimForm(forms.ModelForm):
    class Meta:
        model = TargibotBulim
        fields = ['title', 'hudud', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'hudud': forms.TextInput(attrs={'class': 'selects form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Kategoriya',
            'hudud': 'Hudud',
            'file': 'Fayllar',
        }
    
    
    
class TargibotBoshqaForm(forms.ModelForm):
    class Meta:
        model = TargibotBoshqa
        fields = ['title', 'hudud', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'hudud': forms.TextInput(attrs={'class': 'selects form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Kategoriya',
            'hudud': 'Hudud',
            'file': 'Fayllar',
        }