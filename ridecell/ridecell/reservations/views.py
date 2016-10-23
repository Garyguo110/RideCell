from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from ridecell.parking.models import ParkingLocation
from ridecell.reservations.serializers import ReservationSerializer
from ridecell.reservations.models import Reservation


class ReservationPermissions(BasePermission):

    def has_object_permission(self, request, view, obj):
        # check if user is owner
        return request.user == obj.user


class ReservationUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (ReservationPermissions,)


class ReservationCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReservationSerializer

    def create(request, *args, **kwargs):
        parking_location_id = request.request.data.get('parking_location_id')
        if not parking_location_id:
            return Response("Invalid request, required field not set parking_location_id", status=status.HTTP_400_BAD_REQUEST)
        try:
            reservation = Reservation.objects.create(
                parking_location_id=parking_location_id,
                user_id=request.request.user.id
            )
            return Response({'reservation_id': reservation.id}, status=status.HTTP_201_CREATED)
        except:
            return Response('An error has occured when attempting to create the reservation', status=status.HTTP_400_BAD_REQUEST)
