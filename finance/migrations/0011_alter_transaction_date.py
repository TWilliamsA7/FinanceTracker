# Generated by Django 5.2.1 on 2025-05-27 19:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0010_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
