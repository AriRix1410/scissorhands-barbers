from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm

# Create your views here.


@login_required()
def make_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.customer = request.user
            booking_form.save()
            messages.success(request, ('Your testimonial is awaiting approval'))
            return HttpResponseRedirect('/bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings.html', {'form': form })