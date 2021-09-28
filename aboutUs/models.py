from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutUs(models.Model):
    photo = models.ImageField(upload_to='aboutUs-image',blank=True,null=True,verbose_name='Photo')
    description = RichTextUploadingField(blank=True,null=True,verbose_name='Description')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return f'{self.id}'

