from .models import Testimononial
from django import forms


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimononial
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title*'}),
            'content': forms.Textarea(attrs={'placeholder': 'Testimonial*'}),
        }
