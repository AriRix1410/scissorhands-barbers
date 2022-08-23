"""bookingapp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path("bookings/", views.make_booking, name="bookings"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
    path("edit_booking/<booking_id>", views.edit_booking, name="edit_booking"),
    path("cancel_booking/<booking_id>",
         views.cancel_booking, name="cancel_booking"),
]
