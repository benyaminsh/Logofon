from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    phone = models.CharField(max_length=900,null=True,blank=True,verbose_name='Phone')
    gender = models.CharField(max_length=900,blank=True,null=True,verbose_name='Gender')
    news = models.BooleanField(default=False,blank=True,null=True,verbose_name='News')
    block = models.BooleanField(default=False,null=True,blank=True,verbose_name='Block')
    phone_authentication = models.BooleanField(blank=True,null=True,default=False,verbose_name='Phone authentication')
    user_photo = models.ImageField(upload_to='UserPhoto',blank=True,null=True,verbose_name='User photo')

    def __str__(self):
        return f'{self.get_full_name()}'