from django.shortcuts import render, redirect

from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "auth/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Login successful")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect("home")
