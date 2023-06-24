from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers.user_login_serializers import UserLoginSerializer


class UserLoginView(APIView):
    """User can login by using their credentials"""

    def post(self, request):
        phone_number = request.data.get("phone_number")
        password = request.data.get("password")

        if phone_number and password:
            user_login_data = {
                "phone_number": phone_number,
                "password": password
            }
            serializer = UserLoginSerializer(data = user_login_data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(phone_number=phone_number, password=password)
            if user is not None:
                return Response({
                    "status": True,
                    "details": "Login Successful"
                })
            else:
                return Response({
                    "status": False,
                    "details": "Try Again with right credentials"
                })