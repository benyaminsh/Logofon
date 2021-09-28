from django.db import models
from users.models import User


class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Owner')
    slug = models.CharField(max_length=900,blank=True,null=True,verbose_name='slug')
    title = models.CharField(max_length=900,blank=True,null=True,verbose_name='TiTle')
    text = models.TextField(blank=True,null=True,verbose_name='Text')
    image = models.TextField(blank=True,null=True,verbose_name='Image')
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Date')
    status = models.BooleanField(default=False,blank=True,null=True,verbose_name='Status')

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه  ما'



    def __str__(self):
        return f'TiTle : {self.title}'