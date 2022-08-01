from django.shortcuts import render
from django.views import generic
from .models import Testimononial


# Create your views here.


class TestimonialList(generic.ListView):
    model = Testimononial
    queryset = Testimononial.objects.filter(status=1).order_by("-created_on")
    template_name = 'testimonials.html'
