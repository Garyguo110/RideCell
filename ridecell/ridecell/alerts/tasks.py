import datetime

from django.contrib.gis.measure import D
from django.db.models import F

from ridecell.alerts.models import Alert
from ridecell.parking.models import ParkingLocation


# This task is meant to be called periodically every 5 minutes to process alerts
def process_alerts_periodic_task(timestamp=None):
    if not timestamp:
        timestamp = datetime.datetime.now()
    expired_alerts = Alert.objects.filter(status=Alert.OPEN, time_end__lt=timestamp)
    print "marking %s alerts as expired" % expired_alerts.count()
    for alert in expired_alerts:
        alert.status = Alert.EXPIRED
        alert.save()

    open_alerts = Alert.objects.filter(status=Alert.OPEN, time_start__lt=timestamp)
    print "found %s alerts as open" % open_alerts.count()

    for alert in open_alerts:
        if ParkingLocation.objects.filter(
            location__distance_lte=(alert.location, D(m=int(alert.radius))),
            capacity__gt=F('reserved')
        ).count() > 0:
            alert.status = Alert.SENT
            alert.save()
            print "Found an available parking location for alert %s, sending email to %s and marking alert as sent" % (alert.id, alert.user.username)
        else:
            print "No available parking location found for alert %s" % alert.id
