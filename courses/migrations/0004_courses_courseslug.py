# Generated by Django 3.2.5 on 2021-08-22 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_courses_courseprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='CourseSlug',
            field=models.SlugField(blank=True, max_length=999, null=True, verbose_name='آدرس url '),
        ),
    ]
