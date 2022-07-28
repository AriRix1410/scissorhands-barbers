from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Submit"))


class Testimononial(models.Model):
    title = models.CharField(max_length=200, unique=True)
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client_reviews")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Testimonial {self.title} created by {self.name}"
