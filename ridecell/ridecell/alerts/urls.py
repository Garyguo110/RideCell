from django.conf.urls import include, url

from ridecell.alerts.views import AlertCreateView

urlpatterns = [
    url(r'^$', AlertCreateView.as_view()),
]
