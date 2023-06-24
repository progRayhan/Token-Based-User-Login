from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers.user_registration import UserRegistrationSerializer


class UserRegistrationView(APIView):
    """user can register their account"""

    def post(self, request):
         phone_number = request.data.get("phone_number")
         name = request.data.get("name")
         gender = request.data.get("gender")
         password = request.data.get("password")

         if not phone_number:
              return Response({
                   "status": False,
                   "details": "phone number should be given"
              })
         
         user_data = {
              "phone_number": phone_number,
              "name": name,
              "gender": gender,
              "password": password
         }

         serializer = UserRegistrationSerializer(data=user_data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response({
              "status": True,
              "details": "Registration Successfull"
         })

