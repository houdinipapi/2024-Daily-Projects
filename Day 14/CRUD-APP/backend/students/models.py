from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    reg_no = models.CharField(max_length=50)
    course = models.CharField(max_length=150)

