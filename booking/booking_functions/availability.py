import datetime
from booking.models import Booking

def availability_checker(barber, date, time):
    availability_list = []
    booking_list = Booking.objects.filter(barber=barber)
    for booking in booking_list:
        for date in Booking:
            if 