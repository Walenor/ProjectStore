# Generated by Django 2.0.3 on 2018-04-12 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180412_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_in_order',
            name='customer_email',
        ),
        migrations.RemoveField(
            model_name='product_in_order',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='product_in_order',
            name='customer_phone',
        ),
    ]
