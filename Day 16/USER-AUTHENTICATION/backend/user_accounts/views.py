from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user
from .models import OneTimePassword

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

            return Response({
                "data": user,
                "status": "success",
                "message": f"{user['first_name']} registered successfully. Check your email to verify your account"
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            

class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        otpcode = request.data.get("otp")
        try:
            user_code_obj = OneTimePassword.objects.get(code=otpcode)
            user = user_code_obj.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    "status": "success",
                    "message": f"{user.first_name} has been verified successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "failed",
                    "message": "Code is invalid. User has already been verified"
                }, status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Invalid Code! Does not exist. Please check your code and try again"
            }, status=status.HTTP_404_NOT_FOUND)
