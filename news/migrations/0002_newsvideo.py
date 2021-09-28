# Generated by Django 3.2.5 on 2021-08-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=999, null=True, verbose_name='عنوان ویدیو ')),
                ('video', models.FileField(blank=True, null=True, upload_to='News/NewsVideo/', verbose_name='ویدیو ')),
            ],
            options={
                'verbose_name': 'ویدیو',
                'verbose_name_plural': 'افزودن ویدیو',
            },
        ),
    ]