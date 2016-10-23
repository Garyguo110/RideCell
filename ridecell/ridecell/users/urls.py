from django.conf.urls import include, url

from rest_framework.authtoken.views import obtain_auth_token
from ridecell.users.views import UserCreateView, UserProfileUpdateView

urlpatterns = [
    url(r'^$', UserCreateView.as_view()),
    url(r'^access_token/', obtain_auth_token),
    url(r'^(?P<user_id>\d+)/$', UserProfileUpdateView.as_view()),
]
