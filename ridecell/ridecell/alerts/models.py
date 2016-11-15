import datetime
from django.contrib.gis.db import models as geo_models
from django.db import models
from django.db.models.signals import post_save

from ridecell.parking.models import ParkingLocation


def time_end_offset():
    return datetime.datetime.now() + datetime.timedelta(hours=2)


class Alert(models.Model):
    def __unicode__(self):
        return unicode("%s %s %s" % (self.user.username, self.time_start, self.time_end))

    user = models.ForeignKey('auth.User')
    location = geo_models.PointField(srid=4326, help_text="Longitude, Latitude coordinate system", blank=True, null=True)
    radius = models.PositiveIntegerField(help_text="radius from location in meters")
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    # Status Types
    OPEN = '0'
    SENT = '1'
    EXPIRED = '2'

    STATUS_TYPES = (
        (OPEN, 'Open Alert'),
        (SENT, 'Send Alert'),
        (EXPIRED, 'Expired Alert'),
    )
    status = models.CharField(max_length=3,
                              choices=STATUS_TYPES,
                              default=OPEN,
                              db_index=True,)
