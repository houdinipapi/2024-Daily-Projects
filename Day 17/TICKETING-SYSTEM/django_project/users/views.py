from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .form import RegisterCustomerForm

# Create your views here.


# Register a customer
def register_customer(request):
    if request.method == "POST":
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True

            var.save()

            messages.info(
                request, "Account created for " + form.cleaned_data.get("username")
            )

            return redirect("login")
        else:
            messages.warning(request, "Invalid information!")

            return redirect("register_customer")
    else:
        form = RegisterCustomerForm()
        context = {"form": form}

        return render(request, "users/register_customer.html", context)


# Log in the user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, "You are now logged in as " + username)
            return redirect("dashboard")
        else:
            messages.warning(request, "Invalid username or password!")

            return redirect("login")
    else:
        return render(request, "users/login.html")
    

# Log out the user
def logout_user(request):
    logout(request)
    messages.info(request, "You are now logged out!")
    return redirect("login")
