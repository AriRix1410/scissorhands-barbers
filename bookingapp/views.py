from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
            messages.success(request, ('Your booking is awaiting confirmation'))
            return HttpResponseRedirect('/bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings.html', {'form': form})


@login_required
def my_bookings(request):
    if Booking.objects.filter(approved=True):
        context = {}
        booking_data = Booking.objects.filter(customer=User.objects.get(
            username=request.user)).order_by("date")
        context['booking_data'] = booking_data
        return render(request, 'my_bookings.html', context)
    else:
        return "You have no available bookings"


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.customer = request.user
            booking_form.save()
            messages.success(request, ('Your booking is awaiting confirmation'))
            return redirect('my_bookings')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)

