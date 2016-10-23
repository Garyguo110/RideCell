import re
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated
from rest_framework.response import Response

from ridecell.users.models import UserProfile
from ridecell.users.serializers import UserProfileSerializer, UserSerializer


class UserCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(request, *args, **kwargs):
        data = request.request.data
        serialized = UserSerializer(data=data)
        if serialized.is_valid():
            user, created = User.objects.get_or_create(username=serialized.data['username'])
            if not created:
                return Response("An error has occured when attempting to create the user", status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serialized.data['password'])
            user.save()
            profile = user.userprofile
            phone_number = data.get('phone_number')
            if phone_number:
                phone_number = re.sub("[^0-9]", "", phone_number)
                profile.phone_number = phone_number
                profile.save()

            token = Token.objects.create(user=user)
            return Response({'access_token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfilePermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class UserProfileUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    lookup_field = 'user_id'
    serializer_class = UserProfileSerializer
    permission_classes = (UserProfilePermissions,)

    def perform_update(self, serializer):
        instance = serializer.save()
        # send_email_confirmation(user=self.request.user, modified=instance)