from . import views
from django.urls import path

urlpatterns = [
    path("bookings/", views.make_booking, name="bookings"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
    path("edit_booking/<booking_id>", views.edit_booking, name="edit_booking"),
]