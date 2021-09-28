from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class SiteSettings(models.Model):
    Logo = models.ImageField(upload_to='LogoWebSite',blank=True,null=True,verbose_name='لوگو سایت ')
    background = models.ImageField(upload_to='background',blank=True,null=True,verbose_name='تصویر زمینه ')
    favicon = models.ImageField(upload_to='favicon',blank=True,null=True,verbose_name='آیکون سایت ')
    title = models.CharField(max_length=900,blank=True,null=True,verbose_name='نام سایت ')
    keyWord = models.TextField(blank=True,null=True,verbose_name='کلمه های کلیدی ')
    description = models.TextField(blank=True,null=True,verbose_name='توضیحات سایت ')
    phone = models.CharField(max_length=900,blank=True,null=True,verbose_name='تلفن پشتیبانی ')
    email = models.CharField(max_length=900,blank=True,null=True,verbose_name='ایمیل ')
    toekn_zarinpal = models.TextField(blank=True,null=True,verbose_name='توکن زرین پال ')
    telegram_id = models.CharField(max_length=900, blank=True, null=True, verbose_name='آیدی تلگرام ')
    instagram_id = models.CharField(max_length=900, blank=True, null=True, verbose_name='آیدی اینستاگرام ')
    whatsapp_link = models.CharField(max_length=900, blank=True, null=True, verbose_name='لینک واتساپ ')
    youtube_link = models.TextField(blank=True, null=True,verbose_name='لینک یوتیوب ')
    address_sms = models.CharField(max_length=90,blank=True,null=True,verbose_name='آدرس پنل اسمس ')
    number_sms = models.CharField(max_length=900,blank=True,null=True,verbose_name='شماره پنل اسمس ')
    username_sms = models.CharField(max_length=900,blank=True,null=True,verbose_name=' یوزرنیم پنل اسمس ')
    password_sms = models.CharField(max_length=900,blank=True,null=True,verbose_name=' رمز پنل اسمس ')
    terms_and_Conditions = RichTextUploadingField(blank=True,null=True,verbose_name='قوانین و شرایط ')
    address = models.TextField(blank=True,null=True,verbose_name='آدرس ')



    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات سایت'



    def __str__(self):
        return f'{self.title}'
