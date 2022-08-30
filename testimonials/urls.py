"""testimonials URL Configuration
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
    path("testimonials/",
         views.TestimonialList.as_view(), name="testimonials"),
    path("testimonials/write_testimonial/",
         views.write_testimonial, name="write_testimonial"),
    path("edit_testimonial/<testimonial_id>",
         views.edit_testimonial, name="edit_testimonial"),
    path("delete_testimonial/<testimonial_id>",
         views.delete_testimonial, name="delete_testimonial"),
]
