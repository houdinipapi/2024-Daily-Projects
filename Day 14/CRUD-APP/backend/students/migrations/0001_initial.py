# Generated by Django 5.0.2 on 2024-02-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("student_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=150)),
                ("reg_no", models.CharField(max_length=50)),
                ("course", models.CharField(max_length=150)),
            ],
        ),
    ]
