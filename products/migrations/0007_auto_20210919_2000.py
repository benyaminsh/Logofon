# Generated by Django 3.2.5 on 2021-09-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
