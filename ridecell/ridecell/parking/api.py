from django.db import transaction
from ridecell.parking.models import ParkingLocation


def atomic_update_parking_location_reserved(parking_location_id, value):
    try:
        with transaction.atomic():
            parking_location = ParkingLocation.objects.select_for_update().get(id=parking_location_id)
            if parking_location.reserved + value < parking_location.capacity:
                parking_location.reserved = max(parking_location.reserved + value, 0)
                parking_location.save()
                return True
            else:
                return False
    except:
        return False
