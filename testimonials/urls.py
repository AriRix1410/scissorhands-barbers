from . import views
from django.urls import path

urlpatterns = [
    path("testimonials/",
         views.TestimonialList.as_view(), name="testimonials"),
    path("testimonials/write_testimonial/",
         views.write_testimonial, name="write_testimonial"),
]
