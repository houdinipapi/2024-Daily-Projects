# Generated by Django 5.0.2 on 2024-02-22 08:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Students",
            new_name="Student",
        ),
    ]
