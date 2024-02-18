# Generated by Django 5.0.2 on 2024-02-18 12:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("username", models.CharField(max_length=255, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]