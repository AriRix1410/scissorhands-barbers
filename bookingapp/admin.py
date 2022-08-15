from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('customer', 'barber', 'date', 'time')
    search_fields = ['barber', 'date', 'time']
    list_filter = ('approved',)
    actions = ['confirm_booking']

    def confirm_comments(self, request, queryset):
        queryset.update(approved=True)

