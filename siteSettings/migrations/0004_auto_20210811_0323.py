# Generated by Django 3.2.5 on 2021-08-10 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteSettings', '0003_auto_20210718_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='whatsapp',
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='whatsapp_link',
            field=models.CharField(blank=True, max_length=999, null=True, verbose_name='لینک واتساپ '),
        ),
    ]
