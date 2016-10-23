from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'ridecell.parking.views.filter_parking_locations'),
]
