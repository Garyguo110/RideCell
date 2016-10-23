from django.contrib.auth.models import User

from rest_framework import serializers

from ridecell.users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField()
    password = serializers.CharField(min_length=6)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    last4 = serializers.CharField(read_only=True)
    expiration_date = serializers.DateField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('phone_number', 'username', 'last4', 'expiration_date')
