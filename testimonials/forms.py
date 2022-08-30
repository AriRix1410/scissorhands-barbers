'''
Import the required packages
'''
from django import forms
from .models import Testimononial


class TestimonialForm(forms.ModelForm):
    '''
    Creates form fields for testimonials form
    '''
    class Meta:
        '''
        Specifies the model and which form fields are required on the form
        '''
        model = Testimononial
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title*'}),
            'content': forms.Textarea(attrs={'placeholder': 'Testimonial*'}),
        }
