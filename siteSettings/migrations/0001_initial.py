# Generated by Django 3.2.5 on 2021-07-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Logo', models.ImageField(blank=True, null=True, upload_to='LogoWebSite', verbose_name='Logo WebSite')),
                ('name', models.CharField(blank=True, max_length=999, null=True, verbose_name='Site Name')),
                ('phone', models.CharField(blank=True, max_length=999, null=True, verbose_name='Phone')),
                ('email', models.CharField(blank=True, max_length=999, null=True, verbose_name='Email')),
                ('toekn_zarinpal', models.TextField(blank=True, null=True, verbose_name='Token Zarin PaL')),
                ('telegram_id', models.CharField(blank=True, max_length=999, null=True, verbose_name='Telegram')),
                ('instagram_id', models.CharField(blank=True, max_length=999, null=True, verbose_name='Instagram')),
                ('whatsapp', models.CharField(blank=True, max_length=999, null=True, verbose_name='Whatsapp')),
                ('username', models.CharField(blank=True, max_length=999, null=True, verbose_name='UserName - Panel Sms')),
                ('password', models.CharField(blank=True, max_length=999, null=True, verbose_name='Password - Panel Sms')),
                ('number', models.CharField(blank=True, max_length=999, null=True, verbose_name='Number - Panel Sms')),
                ('api', models.TextField(blank=True, null=True, verbose_name='Api - Panel Sms')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'تنظیمات',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
