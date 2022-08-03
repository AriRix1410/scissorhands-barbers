from .models import Booking
import datetime
from django import forms


class DatePicker(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'time', 'barber', 'service',)
        widgets = {
            'date': DatePicker(),
        }
