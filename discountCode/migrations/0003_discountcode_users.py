# Generated by Django 3.2.5 on 2021-08-31 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountCode', '0002_auto_20210901_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountcode',
            name='users',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد استفاده کنندگان  '),
        ),
    ]