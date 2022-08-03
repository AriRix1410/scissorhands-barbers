from .models import Testimononial
from django import forms


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimononial
        fields = ('title', 'content',)
