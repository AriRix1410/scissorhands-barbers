from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

SERVICES = (
        ('Gents Cut', 'Gents Cut'),
        ('Kids Cut', 'Kids Cut'),
        ('Cut and Shave', 'Cut and Shave'),
        ('Shave Only', 'Shave Only'),
        )

TIME_SLOTS = (
        ('9.00 - 9.30', '9.00 - 9.30'),
        ('9.30 - 10.00', '9.30 - 10.00'),
        ('10.00 - 10.30', '10.00 - 10.30'),
        ('10.30 - 11.00', '10.30 - 11.00'),
        ('11.00 - 11.30', '11.00 - 11.30'),
        ('11.30 - 12.00', '11.30 - 12.00'),
        ('12.00 - 12.30', '12.00 - 12.30'),
        ('13.00 - 13.30', '13.00 - 13.30'),
        ('13.30 - 14.00', '13.30 - 14.00'),
        ('14.00 - 14.30', '14.00 - 14.30'),
        )

BARBER_NAME = (
        ('Nathan', 'Nathan'),
        ('Chris', 'Chris'),
        ('Ben', 'Ben'),
        ('Dan', 'Dan'),
        )


class Booking(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=50, null=True, choices=TIME_SLOTS)
    barber = models.CharField(max_length=50, null=True, choices=BARBER_NAME)
    service = models.CharField(max_length=50, null=True, choices=SERVICES)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} has booked {self.service} on {self.date} at {self.time} with {self.barber}"
