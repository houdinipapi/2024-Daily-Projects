from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    grade = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default="admin")

    def __str__(self):
        return self.first_name