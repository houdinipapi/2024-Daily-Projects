from django.shortcuts import render, redirect

from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
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