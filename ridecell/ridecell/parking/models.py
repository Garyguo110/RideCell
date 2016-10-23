from django.db import models
from django.contrib.gis.db import models as geo_models


class ParkingLocation(models.Model):
    def __unicode__(self):
        return unicode(self.description)

    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.PositiveIntegerField(default=0, help_text="The amount in cents to be charged per hour")
    location = geo_models.PointField(srid=4326, help_text="Longitude, Latitude coordinate system")
    capacity = models.PositiveIntegerField(default=0, help_text="The number of available lots")
    reserved = models.PositiveIntegerField(default=0, help_text="The number of used lots")
