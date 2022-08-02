from django.shortcuts import render
from django.views import generic
from .models import Testimononial


# Create your views here.


class TestimonialList(generic.ListView):
    model = Testimononial
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        context = {}
        list_data = Testimononial.objects.filter(approved=True).order_by("-created_on")
        context['list_data'] = list_data
        return render(request, 'testimonials.html', context)
