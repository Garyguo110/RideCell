from django.conf.urls import include, url

from ridecell.reservations.views import ReservationCreateView, ReservationUpdateView

urlpatterns = [
    url(r'^$', ReservationCreateView.as_view()),
    url(r'^(?P<pk>\d+)/$', ReservationUpdateView.as_view()),
]
