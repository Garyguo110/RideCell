import datetime
from django.contrib.gis.geos import GEOSGeometry

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from ridecell.alerts.serializers import AlertSerializer
from ridecell.alerts.models import Alert


class AlertCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AlertSerializer

    def create(request, *args, **kwargs):
        data = request.request.data
        try:
            location = GEOSGeometry('POINT(%s %s)' % (float(data['longitude']), float(data['latitude'])), srid=4326)
        except:
            return Response("Improper location data passed into endpoint", status=status.HTTP_400_BAD_REQUEST)

        data['user'] = request.request.user.id
        serialized = AlertSerializer(data=data)
        if serialized.is_valid():
            alert = serialized.save()
            alert.location = location
            alert.save(update_fields=['location'])
            return Response({'alert_id': alert.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
