from django.conf.urls import include, url

from ridecell.reservations.views import (
    ReservationCreateView,
    ReservationExtendView,
    ReservationUpdateView,
    ReservationListView
)

urlpatterns = [
    url(r'^$', ReservationCreateView.as_view()),
    url(r'^(?P<pk>\d+)/$', ReservationUpdateView.as_view()),
    url(r'^(?P<pk>\d+)/extend/$', ReservationExtendView.as_view()),
    url(r'^history/$', ReservationListView.as_view()),
]
