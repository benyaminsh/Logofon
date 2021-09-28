from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length=900,blank=True,null=True,verbose_name='عنوان ')
    keyWord = models.TextField(blank=True,null=True,verbose_name='کلمه های کلیدی ')
    image = models.ImageField(upload_to='blogImage',blank=True,null=False,verbose_name='تصویر ')
    Pubdate = models.DateTimeField(auto_created=True,blank=True,null=True,verbose_name='تاریخ ')
    slug = models.CharField(max_length=900,blank=True,null=True,unique=True,verbose_name='آدرس url وبلاگ')
    content = RichTextUploadingField(blank=True,null=True,verbose_name='توضیحات ')

    class Meta:
        verbose_name = 'مطلب'
        verbose_name_plural = 'وبلاگ'


    def __str__(self):
        return f'{self.title}'