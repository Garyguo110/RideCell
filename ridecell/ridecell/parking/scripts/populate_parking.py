from django.contrib.gis.geos import GEOSGeometry

from ridecell.parking.models import ParkingLocation


def create_parking_location(description, longitude, latitude, price=100):
    p = ParkingLocation()
    p.description = description
    p.location = GEOSGeometry('POINT(%s %s)' % (longitude, latitude), srid=4326)
    p.price = price
    p.save()

create_parking_location('Toronto Parking Lot A', -79.431089, 43.76139)
create_parking_location('Toronto Parking Lot B', -79.432089, 43.76139)
create_parking_location('Toronto Parking Lot C', -79.433089, 43.76139)
create_parking_location('Toronto Parking Lot D', -79.434089, 43.76139)
create_parking_location('Toronto Parking Lot $2/hr', -79.430089, 43.76139, price=200)
create_parking_location('Toronto Parking Lot $3/hr', -79.430089, 43.76139, price=300)
create_parking_location('Toronto Parking Lot $4/hr', -79.430089, 43.76139, price=400)
create_parking_location('Toronto Parking Lot $5/hr', -79.430089, 43.76139, price=500)
