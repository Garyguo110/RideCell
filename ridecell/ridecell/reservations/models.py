from django.db import models


class Reservation(models.Model):
    def __unicode__(self):
        return unicode("%s %s %s" % (self.user.username, self.parking_location.description, self.time_created))

    user = models.ForeignKey('auth.User')
    parking_location = models.ForeignKey('parking.ParkingLocation')
    time_created = models.DateTimeField(auto_now_add=True)
