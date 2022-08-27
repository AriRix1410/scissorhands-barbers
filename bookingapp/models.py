import datetime
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

SERVICES = (
    ('', 'Service'),
    ('Gents Cut', 'Gents Cut'),
    ('Kids Cut', 'Kids Cut'),
    ('Cut and Shave', 'Cut and Shave'),
    ('Shave Only', 'Shave Only'),
)

TIME_SLOTS = (
    ('', 'Time Slot'),
    ('9.00 - 10.00', '9.00 - 10.00'),
    ('10.00 - 11.00', '10.00 - 11.00'),
    ('11.00 - 12.00', '11.00 - 12.00'),
    ('12.00 - 13.00', '12.00 - 13.00'),
    ('13.00 - 14.00', '13.00 - 14.00'),
    ('14.00 - 15.00', '14.00 - 15.00'),
    ('15.00 - 16.00', '15.00 - 16.00'),
    ('16.00 - 17.00', '16.00 - 17.00'),
    ('17.00 - 18.00', '17.00 - 18.00'),
)

BARBER_NAME = (
    ('', 'Barber Name'),
    ('Nathan', 'Nathan'),
    ('Chris', 'Chris'),
    ('Ben', 'Ben'),
    ('Dan', 'Dan'),
)


class Booking(models.Model):
    date = models.DateField(
        validators=[MinValueValidator(datetime.date.today)])
    time = models.CharField(max_length=50, null=True, choices=TIME_SLOTS)
    barber = models.CharField(max_length=50, null=True, choices=BARBER_NAME)
    service = models.CharField(max_length=50, null=True, choices=SERVICES)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.customer} has booked {self.service}\
             on {self.date} at {self.time} with {self.barber}"
