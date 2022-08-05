# Generated by Django 3.2.14 on 2022-08-05 00:03

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20220803_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today)]),
        ),
    ]
