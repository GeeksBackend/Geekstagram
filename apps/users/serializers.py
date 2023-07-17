from rest_framework import serializers
from django.contrib.auth import password_validation

from apps.users.models import User
from apps.posts.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'date_joined',
                  'profile_image')

class UserDetailSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(read_only=True, many=True)
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'date_joined',
                  'profile_image', 'user_posts')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=30, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=30, write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'profile_image', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        if attrs['username'] == attrs['password']:
            raise serializers.ValidationError({'username':'Пароль похож на имя пользователя'})
        # Используйте функцию validate_password, чтобы применить все валидаторы пароля.
        password_validation.validate_password(attrs['password'], self.instance)
        return attrs

    def create(self, validated_data:dict):
        print(validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            profile_image=validated_data['profile_image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user