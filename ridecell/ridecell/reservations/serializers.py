from django.contrib.auth.models import User

from rest_framework import serializers

from ridecell.parking.models import ParkingLocation
from ridecell.reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    parking_location = serializers.PrimaryKeyRelatedField(queryset=ParkingLocation.objects.all())

    class Meta:
        model = Reservation
        fields = ('parking_location', 'user', 'id', 'time_created', 'time_end')
