from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from django.contrib.auth.decorators import login_required
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()  # Get all records
    # Check to see if logging in
    if request.method == "POST":
        # Get the username and password
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # If user is not None, then log them in
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password!")
            return redirect("home")

    else:
        return render(request, "home.html", {"records": records})


# def login_user(request):
#     pass


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user
            form.save()

            # Get the username and password
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # Login the user
            login(request, user)

            messages.success(request, "You have successfully registered!")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


# @login_required
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "You need to log in first!")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save(commit=False)
                record.user = request.user
                record.save()
                messages.success(request, "Record added successfully!")
                return redirect("home")
        return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You need to log in first!")
        return redirect("home")
    

def edit_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect("home")
        return render(request, "edit_record.html", {"form": form})
    else:
        messages.success(request, "You need to log in first!")
        return redirect("home")
    


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect("home")
    else:
        messages.success(request, "You need to log in first!")
        return redirect("home")
