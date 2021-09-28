# Generated by Django 3.2.5 on 2021-07-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital_or_physical',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is it a physical product?'),
        ),
    ]
