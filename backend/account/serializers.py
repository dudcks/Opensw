from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            realname=validated_data['realname'],
            password=validated_data['password'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            major=validated_data['major'],
            about_me=validated_data['about_me'],
            username=validated_data['username'],
        )
        return user
    class Meta:
        model = User
        fields = ['id','password','username','email', 'realname', 'age', 'about_me', 'major','gender']