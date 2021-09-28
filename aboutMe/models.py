from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutMe(models.Model):
    name = models.CharField(max_length=900,blank=True,null=True,verbose_name='نام ')
    keyWord = models.TextField(blank=True,null=True,verbose_name='کلمه های کلیدی ')
    image = models.ImageField(upload_to='AboutMe',blank=True,null=True,verbose_name='تصویر ')
    descriptions = RichTextUploadingField(blank=True,null=True,verbose_name='توضیحات ')

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'


    def __str__(self):
        return f'{self.name}'