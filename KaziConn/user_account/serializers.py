from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'userName', 'firstName', 'lastName', 
            'profile_picture', 'identificationNumber', 'phoneNumber', 
            'address', 'createdAt', 'updatedAt', 'lastLogin', 
            'isActive', 'isVerified', 'failed_login_attempts', 
            'account_locked_until', 'is_banned', 'is_staff', 
            'is_service_provider', 'is_admin'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'profile_picture': {'required': False}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Only update fields that are provided
        instance.email = validated_data.get('email', instance.email)
        instance.userName = validated_data.get('userName', instance.userName)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.identificationNumber = validated_data.get('identificationNumber', instance.identificationNumber)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.address = validated_data.get('address', instance.address)
        instance.isActive = validated_data.get('isActive', instance.isActive)
        instance.isVerified = validated_data.get('isVerified', instance.isVerified)
        instance.failed_login_attempts = validated_data.get('failed_login_attempts', instance.failed_login_attempts)
        instance.account_locked_until = validated_data.get('account_locked_until', instance.account_locked_until)
        instance.is_banned = validated_data.get('is_banned', instance.is_banned)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_service_provider = validated_data.get('is_service_provider', instance.is_service_provider)
        instance.is_admin = validated_data.get('is_admin', instance.is_admin)
        instance.save()
        return instance
