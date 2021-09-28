# Generated by Django 3.2.5 on 2021-08-14 23:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students', models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد دانشجویان ')),
                ('videos', models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد ویدیو ها ')),
                ('CourseLevel', models.CharField(blank=True, default='مقدماتی', max_length=999, null=True, verbose_name='سطح دوره ')),
                ('CourseStatus', models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت دوره : درحال بارگزاری / به اتمام رسیده ')),
                ('CourseName', models.CharField(blank=True, max_length=999, null=True, verbose_name='نام دوره ')),
                ('CourseImage', models.ImageField(blank=True, null=True, upload_to='CourseImage', verbose_name='تصویر دوره ')),
                ('CourseDescription', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='توضیحات دوره ')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
            },
        ),
    ]
