'''
Import the required packages
'''
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    '''
    Posts the bookings form
    '''
    list_display = ('customer', 'barber', 'date', 'time')
    search_fields = ['barber', 'date', 'time']
    list_filter = ('approved',)
    actions = ['confirm_booking']

    # pylint: disable=unused-argument
    def confirm_booking(self, request, queryset):
        '''
        Allows admin to select approve from action drop down
        '''
        queryset.update(approved=True)
