'''
Import the required packages
'''
import datetime
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    '''
    Creates form fields for bookings form
    '''
    class Meta:
        '''
        Specifies the model and which form fields are required on the form
        '''
        model = Booking
        fields = ('date', 'time', 'barber', 'service',)
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'min': datetime.datetime.now().date()}),
        }
