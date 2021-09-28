# Generated by Django 3.2.5 on 2021-07-17 20:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=220, unique=True)),
                ('discount_percent', models.IntegerField(blank=True, default=1, null=True, verbose_name='discount percent : 10% ')),
                ('price', models.IntegerField(default=0)),
                ('discount_price', models.IntegerField(default=0)),
                ('digital_or_physical', models.BooleanField(blank=True, default=False, null=True, verbose_name='Digital or physical ?')),
                ('in_stock', models.BooleanField(blank=True, default=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ebook', models.FileField(blank=True, null=True, upload_to='fp')),
                ('category', models.ManyToManyField(related_name='Categories', to='categories.Categories')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]