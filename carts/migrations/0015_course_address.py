# Generated by Django 3.2.5 on 2021-08-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0014_auto_20210822_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس '),
        ),
    ]