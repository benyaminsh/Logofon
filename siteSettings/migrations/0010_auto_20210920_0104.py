# Generated by Django 3.2.5 on 2021-09-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSettings', '0009_auto_20210920_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='password_sms',
            field=models.CharField(blank=True, max_length=999, null=True, verbose_name=' رمز پنل اسمس '),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='username_sms',
            field=models.CharField(blank=True, max_length=999, null=True, verbose_name=' یوزرنیم پنل اسمس '),
        ),
    ]
