# Generated by Django 3.2.5 on 2021-08-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_courseprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='CoursePrice',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='قیمت دوره '),
        ),
    ]
