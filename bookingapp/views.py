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
    '''
    Posts data to bookings. Renders the
    bookings page.
    '''
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.customer = request.user
            booking_form.save()
            messages.success(
                request, ('Your request has been sent and is awaiting\
                     confirmation'))
            return HttpResponseRedirect('/bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings.html', {'form': form})


@login_required
def my_bookings(request):
    '''
    Gets objects from bookings. If the username of the booking
    is the same as the request user then any approved bookings
    will be displayed. Renders the my bookings page.
    '''
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
    '''
    Gets the stored data by id for a specific confirmed
    booking and allows for editing. Resubmission sets the
    approved back to false for it to be confirmed again by
    the admin. Renders edit bookings page.
    '''
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.customer = request.user
            booking_form.approved = False
            booking_form.save()
            messages.success(
                request, ('Your booking is awaiting confirmation'))
            return redirect('my_bookings')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


@login_required
def cancel_booking(request, booking_id):
    '''
    Gets stored booking data by booking id and allows
    the user to cancel the booking
    '''
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('my_bookings')
