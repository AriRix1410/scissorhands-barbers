from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Testimononial
from .forms import TestimonialForm


# Create your views here.


class TestimonialList(generic.ListView):
    model = Testimononial
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        # context = {}
        # list_data = Testimononial.objects.filter(
        #     approved=True).order_by("-created_on")
        # context['list_data'] = list_data

        paginate = Paginator(Testimononial.objects.filter(
            approved=True).order_by("-created_on"), 1)
        page = request.GET.get('page')
        lists = paginate.get_page(page)

        return render(request, 'testimonials.html', {'lists':lists})


@login_required()
def write_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial_form = form.save(commit=False)
            testimonial_form.name = request.user
            testimonial_form.save()
            messages.success(
                request, ('Your testimonial is awaiting approval'))
            return HttpResponseRedirect('/testimonials')
    else:
        form = TestimonialForm()

    return render(request, 'write_testimonial.html', {'form': form})
