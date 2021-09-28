# Generated by Django 3.2.5 on 2021-08-22 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0013_remove_course_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=999, null=True, verbose_name='آدرس url '),
        ),
        migrations.AddField(
            model_name='digital',
            name='slug',
            field=models.SlugField(blank=True, max_length=999, null=True, verbose_name='آدرس url '),
        ),
        migrations.AddField(
            model_name='physical',
            name='slug',
            field=models.SlugField(blank=True, max_length=999, null=True, verbose_name='آدرس url '),
        ),
    ]
