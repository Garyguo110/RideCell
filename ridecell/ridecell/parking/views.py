from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ridecell.parking.models import ParkingLocation
from ridecell.parking.serializers import ParkingLocationSerializer


class ParkingLocationListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = ParkingLocation.objects.all()
    serializer_class = ParkingLocationSerializer

    def list(request, *args, **kwargs):
        query_params = request.request.query_params
        longitude = query_params.get('longitude')
        latitude = query_params.get('latitude')
        distance = query_params.get('distance')
        price = query_params.get('price')

        queryset = request.get_queryset()
        if latitude and longitude and distance:
            pnt = GEOSGeometry('POINT(%s %s)' % (longitude, latitude), srid=4326)
            queryset = queryset.filter(location__distance_lte=(pnt, D(m=int(distance))))
        if price:
            queryset = queryset.filter(price__lte=price)

        serializer = ParkingLocationSerializer(queryset, many=True)
        return Response(serializer.data)
