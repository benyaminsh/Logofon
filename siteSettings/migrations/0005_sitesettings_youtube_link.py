# Generated by Django 3.2.5 on 2021-08-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSettings', '0004_auto_20210811_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='youtube_link',
            field=models.TextField(blank=True, null=True, verbose_name='لینک یوتیوب '),
        ),
    ]