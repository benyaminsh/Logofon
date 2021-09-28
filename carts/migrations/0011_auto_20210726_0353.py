# Generated by Django 3.2.5 on 2021-07-25 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0010_auto_20210726_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalordering',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digitalordering_set', to='carts.cart', verbose_name='خریدار '),
        ),
        migrations.AlterField(
            model_name='physicalproducts',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='physicalproducts_set', to='carts.cart', verbose_name='خریدار '),
        ),
    ]