from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'ridecell.main.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('ridecell.users.urls')),
    url(r'^parking/', include('ridecell.parking.urls')),
    url(r'^reservations/', include('ridecell.reservations.urls')),
]
