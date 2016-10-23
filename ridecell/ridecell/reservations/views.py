from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from ridecell.parking.api import atomic_update_parking_location_reserved
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

    def destroy(request, *args, **kwargs):
        reservation = Reservation.objects.get(id=kwargs.get('pk'))
        atomic_update_parking_location_reserved(reservation.parking_location_id, -1)
        return super(ReservationUpdateView, request).destroy(request.request, *args, **kwargs)

    def update(request, *args, **kwargs):
        parking_location_id = request.request.data.get('parking_location')
        reservation = Reservation.objects.get(id=kwargs.get('pk'))
        if parking_location_id != reservation.parking_location_id:
            succeeded = atomic_update_parking_location_reserved(parking_location_id, 1)
            if succeeded:
                atomic_update_parking_location_reserved(reservation.parking_location_id, -1)
            else:
                return Response('An error has occured when attempting to create the reservation', status=status.HTTP_400_BAD_REQUEST)
        return super(ReservationUpdateView, request).update(request.request, *args, **kwargs)


class ReservationCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReservationSerializer

    def create(request, *args, **kwargs):
        parking_location_id = request.request.data.get('parking_location')
        succeeded = atomic_update_parking_location_reserved(parking_location_id, 1)
        if not succeeded:
            return Response('An error has occured when attempting to create the reservation', status=status.HTTP_400_BAD_REQUEST)
        reservation = Reservation.objects.create(
            parking_location_id=parking_location_id,
            user_id=request.request.user.id
        )
        return Response({'reservation_id': reservation.id}, status=status.HTTP_201_CREATED)
