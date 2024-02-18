from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.forms import ValidationError
from web_sec_app.models import Search
from web_sec_project.settings import FILE_UPLOAD_ALLOWED_EXTENSIONS

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

@user_passes_test(lambda u: u.is_superuser)
def admin(request):
    return render(
        request,
        "admin.html",
        {
            "username": request.user.username,
        })


def search(request):
    query = request.GET.get("q")
    if query is not None:
        results = Search.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    else:
        results = []
    return render(
        request,
        "search.html",
        {
            "results": results,
        })


def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
            if uploaded_file.content_type in FILE_UPLOAD_ALLOWED_EXTENSIONS:
                try:
                    with open("uploads/" + uploaded_file.name, "wb+") as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                    return render(
                        request,
                        "success.html"
                    )
                except ValidationError as e:
                    error_message = str(e)
                    return render(
                        request,
                        "fileUpload.html",
                        {
                            "error_message": error_message,
                        }
                    )
            else:
                error_message = "Invalid file type!"
                return render(
                    request,
                    "fileUpload.html",
                    {
                        "error_message": error_message,
                    }
                )
        else:
            error_message = "No file uploaded!"
            return render(
                request,
                "fileUpload.html",
                {
                    "error_message": error_message,
                }
            )
    else:
        return render(
            request,
            "fileUpload.html"
        )