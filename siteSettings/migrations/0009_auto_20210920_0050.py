# Generated by Django 3.2.5 on 2021-09-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSettings', '0008_auto_20210914_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='token_sms',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='address_sms',
            field=models.CharField(blank=True, max_length=999, null=True, verbose_name='آدرس پنل اسمس '),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='password_sms',
            field=models.TextField(blank=True, null=True, verbose_name=' رمز پنل اسمس '),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='username_sms',
            field=models.TextField(blank=True, null=True, verbose_name=' یوزرنیم پنل اسمس '),
        ),
    ]
