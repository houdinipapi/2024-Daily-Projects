from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import (
    UserRegisterSerializer,
    LoginSerializer,
    PasswordResetRequestSerializer,
    SetNewPasswordSerializer,
    LogoutUserSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user
from .models import OneTimePassword
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User


# Create your views here.


class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data
            # TODO: Send email to user
            send_code_to_user(user["email"])

            return Response(
                {
                    "data": user,
                    "status": "success",
                    "message": f"{user['first_name']} registered successfully. Check your email to verify your account",
                },
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        otpcode = request.data.get("otp")
        try:
            user_code_obj = OneTimePassword.objects.get(code=otpcode)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(
                    {
                        "status": "success",
                        "message": f"{user.first_name} has been verified successfully",
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "status": "failed",
                        "message": "Code is invalid. User has already been verified",
                    },
                    status=status.HTTP_204_NO_CONTENT,
                )
        except OneTimePassword.DoesNotExist:
            return Response(
                {
                    "status": "failed",
                    "message": "Invalid Code! Does not exist. Please check your code and try again",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={
                "request": request},
        )
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TestAuthenticationView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "status": "success",
            "message": "User is authenticated"
        }

        return Response(data, status=status.HTTP_200_OK)


class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={
                "request": request
            }
        )

        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "status": "success",
                "message": "Check your email for the password reset link"
            },
            status=status.HTTP_200_OK
        )
    

class PasswordResetConfirm(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {
                        "status": "failed",
                        "message": "Token is invalid, please request a new one"
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            else:
                return Response(
                    {
                        "success": True,
                        "status": "success",
                        "message": "Credentials are valid",
                        "uidb64": uidb64,
                        "token": token
                    },
                    status=status.HTTP_200_OK
                )
            
        except DjangoUnicodeDecodeError:
            return Response(
                {
                    "status": "failed",
                    "message": "Token is invalid, please request a new one"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        

class SetNewPassword(GenericAPIView):
    serializer_class  = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "status": "success",
                "message": "Password reset successful"
            },
            status=status.HTTP_200_OK
        )
    

class LogoutUserView(GenericAPIView):
    serializer_class = LogoutUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "status": "success",
                "message": "User has been logged out"
            },
            status=status.HTTP_200_OK
        )
