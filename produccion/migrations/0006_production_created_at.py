# Generated by Django 5.1.4 on 2025-01-22 21:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0005_alter_production_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
