from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=900,blank=True,null=True,verbose_name='عنوان اخبار ')
    photo = models.ImageField(upload_to='News/NewsPhoto/',blank=True,null=True,verbose_name='تصویر ')
    video = models.FileField(upload_to='News/NewsVideo/',blank=True,null=True,verbose_name='ویدیو ')
    voice = models.FileField(upload_to='News/NewsVoice/',blank=True,null=True,verbose_name='صدا ')
    text = RichTextUploadingField(blank=True,null=True,verbose_name='متن ')

    class Meta:
        verbose_name = 'اخبار'
        verbose_name_plural = 'افزودن اخبار'


    def __str__(self):
        return f'{self.title}'




