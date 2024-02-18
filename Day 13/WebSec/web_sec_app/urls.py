from django.urls import path
from . import views


urlpatterns = [
    path("", views.user_view, name="create_user"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("search/", views.search, name="search"),
    path("upload/", views.upload_file, name="upload"),
]