from django.conf.urls import include, url

from ridecell.parking.views import ParkingLocationListView

urlpatterns = [
    url(r'^$', ParkingLocationListView.as_view()),
]
