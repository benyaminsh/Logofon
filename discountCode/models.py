from users.models import User
from django.db import models

class DiscountCode(models.Model):
    code = models.CharField(max_length=900,blank=True,null=True,verbose_name='کد ')
    discount_percent = models.IntegerField(default=0,blank=True,null=True,verbose_name='قیمت تخفیف  ')
    users = models.IntegerField(default=0,blank=True,null=True,verbose_name='تعداد استفاده کنندگان  ')

    class Meta:
        verbose_name = 'کد'
        verbose_name_plural = 'کد تخفیف'

    def __str__(self):
        return f'{self.code}'


class Users_DiscountCode(models.Model): #estfade konande ha az code takhfif
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='استفاده کننده ')
    discount_percent = models.IntegerField(default=0,blank=True,null=True,verbose_name='قیمت تخفیف  ')
    code = models.CharField(max_length=900,blank=True,null=True,verbose_name='کد ')
    
    class Meta:
        verbose_name = 'استفاده کننده'
        verbose_name_plural = 'استفاده کنندگان'

    def __str__(self):
        return f'{self.code}'