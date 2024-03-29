# Generated by Django 3.2.5 on 2021-07-25 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20210718_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalordering',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Digitalordering_set', to='carts.cart', verbose_name='خریدار '),
        ),
        migrations.AlterField(
            model_name='physicalproducts',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Physicalproducts_set', to='carts.cart', verbose_name='خریدار '),
        ),
    ]
