from rest_framework import serializers 
from .models import User

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=["user_name","email","phone_number","password","address"]
        
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user