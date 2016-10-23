from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html", content_type='text/html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('ridecell.users.urls')),
    url(r'^parking/', include('ridecell.parking.urls')),
    url(r'^reservations/', include('ridecell.reservations.urls')),
]
