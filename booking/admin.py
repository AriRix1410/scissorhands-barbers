from django.contrib import admin
from .models import Customer, Barber, Booking

# Register your models here.


admin.site.register(Customer)
admin.site.register(Barber)
admin.site.register(Booking)
