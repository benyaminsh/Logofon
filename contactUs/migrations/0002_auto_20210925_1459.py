# Generated by Django 3.2.5 on 2021-09-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(blank=True, max_length=900, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(blank=True, max_length=900, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=900, null=True, verbose_name='Subject'),
        ),
    ]
