from ridecell.parking.models import ParkingLocation
from rest_framework import serializers


class ParkingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLocation
        fields = ('description', 'id', 'location', 'price', 'reserved', 'capacity')
