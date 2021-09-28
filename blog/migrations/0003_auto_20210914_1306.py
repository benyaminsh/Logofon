# Generated by Django 3.2.5 on 2021-09-14 08:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_timeread'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='keyWord',
            field=models.TextField(blank=True, null=True, verbose_name='کلمه های کلیدی '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Pubdate',
            field=models.DateTimeField(auto_created=True, blank=True, null=True, verbose_name='تاریخ '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='توضیحات '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='blogImage', verbose_name='تصویر '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=999, null=True, unique=True, verbose_name='آدرس url وبلاگ'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=999, null=True, verbose_name='عنوان '),
        ),
    ]