'''
Import the required packages
'''
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.


class MakeBookingTestCase(TestCase):
    def setUp(self):
        self.username = "user"
        self.password = "valid_password1"
        self.client = Client()
        self.url = reverse("bookings")

        User.objects.create_user(
            self.username, "email@test.com", self.password)

    def test_bookings_sends_user_to_login(self):
        response = self.client.get(self.url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")
