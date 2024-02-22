# Generated by Django 5.0.2 on 2024-02-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_rename_students_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="student",
            name="created_by",
            field=models.CharField(default="admin", max_length=100),
        ),
    ]