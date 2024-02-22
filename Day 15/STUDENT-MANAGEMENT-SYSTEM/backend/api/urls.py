from django.urls import path
from .views import StudentListCreate, StudentDetailView

urlpatterns = [
    path("students/", StudentListCreate.as_view(), name="student-list-create"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
]