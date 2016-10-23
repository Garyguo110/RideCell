from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ridecell.parking.models import ParkingLocation
from ridecell.parking.serializers import ParkingLocationSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
def filter_parking_locations(request):
    query_params = request.query_params
    longitude = query_params.get('longitude')
    latitude = query_params.get('latitude')
    distance = query_params.get('distance')
    price = query_params.get('price')

    parking_locations = ParkingLocation.objects.all()
    if latitude and longitude and distance:
        pnt = GEOSGeometry('POINT(%s %s)' % (longitude, latitude), srid=4326)
        parking_locations = parking_locations.filter(location__distance_lte=(pnt, D(m=int(distance))))
    if price:
        parking_locations = parking_locations.filter(price__lte=price)

    serializer = ParkingLocationSerializer(parking_locations, many=True)
    return Response(serializer.data)
