from rest_framework.serializers import ModelSerializer

from user.models import User

class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        