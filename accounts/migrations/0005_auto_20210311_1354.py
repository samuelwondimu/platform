# Generated by Django 3.1.7 on 2021-03-11 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_auto_20210311_1351"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="graduation_year",
            field=models.PositiveIntegerField(
                null=True, validators=[django.core.validators.MinValueValidator(1740)]
            ),
        ),
    ]
