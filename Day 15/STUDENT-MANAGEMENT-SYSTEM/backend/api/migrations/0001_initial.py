# Generated by Django 5.0.2 on 2024-02-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("grade", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("phone", models.CharField(max_length=50)),
                ("address", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
