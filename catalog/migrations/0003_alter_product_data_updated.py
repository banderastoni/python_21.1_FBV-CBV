# Generated by Django 5.0 on 2023-12-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_product_is_active_product_data_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='data_updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
