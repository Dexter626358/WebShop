# Generated by Django 2.0.3 on 2018-04-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20180413_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product_in_cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]