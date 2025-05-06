from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, RegexValidator
from fernet_fields import EncryptedCharField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator



class CategoryAJ(models.Model):
    title = models.IntegerField(
        verbose_name="modda",
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )
    sup = models.IntegerField(
        verbose_name="bandi",
        blank=True,
        null=True,
        validators=[MaxValueValidator(999), MinValueValidator(0)]
    )   
    
    class Meta:
        verbose_name = "Aniqlangan-jinoyatlar Kategorya"
        verbose_name_plural = "Aniqlangan-jinoyatlar Kategorya"
    
    def __str__(self):
        if self.sup is not None:
            return f"{self.title} {self.sup}"
        return f"{self.title}"
    
    
  
    


# Umumiy abstrakt model
class BaseModel(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Bank Model
class BankModel(BaseModel):
    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banklar"


# Tashkilot Model
class TashkilotModel(BaseModel):
    class Meta:
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlar"


# Hudud Model
class HududModel(BaseModel):
    class Meta:
        verbose_name = "Hudud"
        verbose_name_plural = "Hududlar"


# Jinoyat Model
class JinoyatModel(BaseModel):
    class Meta:
        verbose_name = "Jinoyat"
        verbose_name_plural = "Jinoyatlar"


# Ilova Model
class IlovaModel(BaseModel):
    class Meta:
        verbose_name = "Ilova"
        verbose_name_plural = "Ilovalar"


# Xitr Model
class XitrModel(BaseModel):
    class Meta:
        verbose_name = "Sodir etish usuli"
        verbose_name_plural = "Sodir etish usullari"


# Natija Model
class ResultModel(BaseModel):
    class Meta:
        verbose_name = "Natija holati"
        verbose_name_plural = "Natija holatlari"




# Jobs Model
class JobsModel(BaseModel):
    class Meta:
        verbose_name = "Kasb"
        verbose_name_plural = "Kasblar"



class AJ_article(models.Model):
    hudud = models.ForeignKey(HududModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryAJ, on_delete=models.CASCADE, verbose_name="Jinoyat turi")
    data = models.DateField(auto_now=False,)
    files = models.FileField(upload_to='Aniqlangan-jinoyatlar-fayl/', verbose_name="murijat fayli")
  
    class Meta:
        verbose_name = "Aniqlangan Jinoyatlar"
        verbose_name_plural = "Aniqlangan Jinoyatlar"

    def __str__(self):
        return f"{self.hudud} ({self.data.strftime('%Y-%m-%d %H:%M')})"




# UserModelInfo Model
class UserModelInfo(models.Model):
    data = models.DateTimeField()
    tashkilot = models.ForeignKey(TashkilotModel, on_delete=models.CASCADE, blank=True)
    hudud = models.ForeignKey(HududModel, on_delete=models.CASCADE)
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    manzil = models.CharField(max_length=350)
    tell = PhoneNumberField(blank=True, null=True)
    holat_mazmuni = models.TextField(blank=True)
    jinoyat = models.ForeignKey(JinoyatModel, on_delete=models.CASCADE)
    jobs = models.ForeignKey(JobsModel, verbose_name="Kasbingizni kiriting", on_delete=models.CASCADE, null=True, blank=True)
    
    
    karta_number = EncryptedCharField(
        max_length=255,
        validators=[RegexValidator(regex=r'^\d{16}$', message="Karta raqami 16 raqamdan iborat")],
        blank=True,
        null=True
    )
    
    bank = models.ForeignKey(BankModel, on_delete=models.CASCADE)
    ilova = models.ForeignKey(IlovaModel, on_delete=models.CASCADE)
    xitr = models.ForeignKey(XitrModel, on_delete=models.CASCADE)
    zarar = models.DecimalField(max_digits=20, decimal_places=5, validators=[MinValueValidator(0)])
    natija = models.ForeignKey(ResultModel, on_delete=models.CASCADE)
    pul_data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    files = models.FileField(upload_to='media/Murijaatlar', verbose_name="murijat fayli PDF da", blank=True)
    

    class Meta:
        verbose_name = "Ro'yxat"
        verbose_name_plural = "Ro'yxatlar"
        ordering = ['-id'] 

    def __str__(self):
        return self.name
    






class Article_FJ(models.Model):
    hudud = models.ForeignKey(HududModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryAJ, on_delete=models.CASCADE, verbose_name="Jinoyat turi")
    data = models.DateField(auto_now=False,)
    files = models.FileField(upload_to='Fosh-etilgan-Jinoyatlar-fayl/', verbose_name="murijat fayli")
  
    class Meta:
        verbose_name = "Fosh-etilgan Jinoyatlar"
        verbose_name_plural = "Fosh-etilgan Jinoyatlar"

    def __str__(self):
        return f"{self.hudud} ({self.data.strftime('%Y-%m-%d %H:%M')})"




class Article_Boshqa_tashkilot(models.Model):
    hudud = models.ForeignKey(HududModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryAJ, on_delete=models.CASCADE, verbose_name="Jinoyat turi")
    data = models.DateField(auto_now=False,)
    files = models.FileField(upload_to='Fosh-etilgan-Jinoyatlar-fayl/', verbose_name="murijat fayli")
  
    class Meta:
        verbose_name = "Boshqa tashkilot Tomonidan"
        verbose_name_plural = "Boshqa tashkilot Tomonidan"

    def __str__(self):
        return f"{self.hudud} ({self.data.strftime('%Y-%m-%d %H:%M')})"
    
    


############################################## 
############################################## 
############################################## 



class TargibotBulim(models.Model):
    title = models.CharField(max_length=150, verbose_name="Targ'ibotchi shaxsi")
    hudud = models.CharField(max_length=350, verbose_name="Targ'ibot o'tgazilgan joy")
    file = models.FileField(upload_to="targ'ibot/", verbose_name="Targ'ibot fayli")
    
    class Meta:
        verbose_name = "Bo'lim Targ'ibot"
        verbose_name_plural = "Bo'lim Targ'ibot"
    
    def __str__(self):
        return self.title
    
    
    
############################################## 
############################################## 
############################################## 

class TargibotBoshqa(models.Model):
    title = models.CharField(max_length=150, verbose_name="Targ'ibotchi shaxsi")
    hudud = models.CharField(max_length=350, verbose_name="Targ'ibot o'tgazilgan joy")
    file = models.FileField(upload_to="targ'ibot/", verbose_name="Targ'ibot fayli")
    
    class Meta:
        verbose_name = "Boshqa tashkilot Targ'iboti"
        verbose_name_plural = "Boshqa tashkilot Targ'iboti"
    
    def __str__(self):
        return self.title
    
