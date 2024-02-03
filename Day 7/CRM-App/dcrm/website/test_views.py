from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.urls import reverse
from .models import Record


class DeleteCustomerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.record = Record.objects.create(name="Test Customer")

    def test_delete_customer_authenticated(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("delete_customer", args=[self.record.id]))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(response.url, reverse("home"))  # Redirect to home page
        self.assertEqual(
            Record.objects.filter(id=self.record.id).exists(), False
        )  # Record should be deleted
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)  # One success message should be displayed
        self.assertEqual(str(messages[0]), "Record deleted successfully!")

    def test_delete_customer_not_authenticated(self):
        response = self.client.post(reverse("delete_customer", args=[self.record.id]))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertEqual(response.url, reverse("home"))  # Redirect to home page
        self.assertEqual(
            Record.objects.filter(id=self.record.id).exists(), True
        )  # Record should not be deleted
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)  # One success message should be displayed
        self.assertEqual(str(messages[0]), "You need to log in first!")
