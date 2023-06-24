from rest_framework.serializers import ModelSerializer

from user.models import User

class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "name", "gender", "password"]