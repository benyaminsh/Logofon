# Generated by Django 3.2.5 on 2021-07-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=999, null=True, verbose_name='Code')),
                ('phone', models.CharField(blank=True, max_length=999, null=True, verbose_name='Phone')),
                ('status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'کد',
                'verbose_name_plural': 'کد های تایید',
            },
        ),
    ]