import datetime
from django.db import models
from django.db.models.signals import post_save

from ridecell.parking.models import ParkingLocation


def time_end_offset():
    return datetime.datetime.now() + datetime.timedelta(hours=2)


class Reservation(models.Model):
    def __unicode__(self):
        return unicode("%s %s %s" % (self.user.username, self.parking_location.description, self.time_created))

    user = models.ForeignKey('auth.User')
    parking_location = models.ForeignKey('parking.ParkingLocation')
    time_created = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(default=time_end_offset)
