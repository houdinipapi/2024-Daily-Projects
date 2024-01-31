from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
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
        return render(request, "home.html", {})


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
        return render(request, "register.html",
                      {
                          "form": form
                        })
    
    return render(request, "register.html",
                  {
                      "form": form
                    })
