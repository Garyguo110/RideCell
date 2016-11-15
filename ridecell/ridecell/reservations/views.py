import datetime
from dateutil import parser

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
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
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (ReservationPermissions, IsAuthenticated)

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


class ReservationListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReservationSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        try:
            start_time = parser.parse(query_params.get('start_datetime'))
        except:
            start_time = None

        try:
            end_time = parser.parse(query_params.get('end_datetime'))
        except:
            end_time = None

        user = self.request.user
        reservations = Reservation.objects.filter(user=user)
        if start_time:
            reservations = reservations.filter(time_created__gte=start_time)
        if end_time:
            reservations = reservations.filter(time_end__lte=end_time)

        return reservations


class ReservationExtendView(UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, ReservationPermissions)

    def partial_update(request, *args, **kwargs):
        reservation = Reservation.objects.get(id=kwargs.get('pk'))
        try:
            extension_in_minutes = int(request.request.data.get('extension_in_minutes'))
        except:
            extension_in_minutes = None

        if extension_in_minutes:
            reservation.time_end += datetime.timedelta(minutes=extension_in_minutes)
            reservation.save(update_fields=['time_end'])
            return Response(
                {
                    'id': reservation.id,
                    'time_end': reservation.time_end
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response('Invalid input for this endpoint', status=status.HTTP_400_BAD_REQUEST)
