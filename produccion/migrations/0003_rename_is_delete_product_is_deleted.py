# Generated by Django 5.1.4 on 2025-01-21 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_product_is_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_delete',
            new_name='is_deleted',
        ),
    ]
