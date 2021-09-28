# Generated by Django 3.2.5 on 2021-08-21 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210811_0434'),
        ('courses', '0001_initial'),
        ('carts', '0011_auto_20210726_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=999, null=True, verbose_name='قیمت ')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت ')),
                ('is_paid', models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت پرداخت ')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس ')),
                ('post_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت ارسال ')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_set', to='carts.cart', verbose_name='خریدار ')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.courses', verbose_name='دوره ')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
            },
        ),
        migrations.CreateModel(
            name='Digital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=999, null=True, verbose_name='قیمت ')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت ')),
                ('is_paid', models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت پرداخت ')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digital_set', to='carts.cart', verbose_name='خریدار ')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول ')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات دیجیتالی',
            },
        ),
        migrations.CreateModel(
            name='Physical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=999, null=True, verbose_name='قیمت ')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت ')),
                ('is_paid', models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت پرداخت ')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس ')),
                ('post_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='وضعیت ارسال ')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='physical_set', to='carts.cart', verbose_name='خریدار ')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول ')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات فیزیکی',
            },
        ),
        migrations.RemoveField(
            model_name='physicalproducts',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='physicalproducts',
            name='product',
        ),
        migrations.DeleteModel(
            name='Digitalordering',
        ),
        migrations.DeleteModel(
            name='Physicalproducts',
        ),
    ]