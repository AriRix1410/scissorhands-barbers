from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SERVICES = (
        ('Gents Cut', 'Gents Cut'),
        ('Kids Cut', 'Kids Cut'),
        ('Cut and Shave', 'Cut and Shave'),
        ('Shave Only', 'Shave Only'),
        )

BARBER_NAME = (
        ('Nathan', 'Nathan'),
        ('Chris', 'Chris'),
        ('Ben', 'Ben'),
        ('Dan', 'Dan'),
        )


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


# class Barber(models.Model):
#     SERVICES = (
#         ('Gents Cut', 'Gents Cut'),
#         ('Kids Cut', 'Kids Cut'),
#         ('Cut and Shave', 'Cut and Shave'),
#         ('Shave Only', 'Shave Only'),
#         )
#     barbername = models.CharField(max_length=50, null=True)
#     service = models.CharField(max_length=50, null=True, choices=SERVICES)

#     def __str__(self):
#         return self.barbername


class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    barber = models.CharField(max_length=50, null=True, choices=BARBER_NAME)
    service = models.CharField(max_length=50, null=True, choices=SERVICES)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} has booked {self.service} on {self.date} at {self.time} with {self.barber}"

