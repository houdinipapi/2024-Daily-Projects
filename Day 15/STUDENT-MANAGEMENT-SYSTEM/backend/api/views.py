from django.shortcuts import render

from rest_framework import generics
from .models import Student
from .serializer import StudentSerializer

# Create your views here.

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer