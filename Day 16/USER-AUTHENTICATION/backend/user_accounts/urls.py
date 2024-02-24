from django.urls import path
from .views import (
    RegisterUserView,
    VerifyUserEmail,
    LoginUserView,
    TestAuthenticationView,
    PasswordResetConfirm,
    PasswordResetRequestView,
    SetNewPassword,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("verify/", VerifyUserEmail.as_view(), name="verify"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("test-auth/", TestAuthenticationView.as_view(), name="test-auth"),
    path("password-reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirm.as_view(), name="password-reset-confirm"),
    path("set-new-password/", SetNewPassword.as_view(), name="set-new-password"),

]
