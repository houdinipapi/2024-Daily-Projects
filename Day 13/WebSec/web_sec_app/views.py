from django.shortcuts import render

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your views here.
def user_view(request):
    users = User.objects.all()
    password = "password"
    hashed_password = make_password(password)

    return render(
        request,
        "create_user.html",
        {
            "users": users,
            "hashed_password": hashed_password,
        }
    )