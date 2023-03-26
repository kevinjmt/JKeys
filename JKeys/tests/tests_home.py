from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client
from django.urls import reverse


"""
LEGEND:
-> In each TestClass:
    V -> Tested
    ~ -> Partially Tested
    - -> Not Tested
"""


class HomePageTests(TestCase):
    """
    Tests for CreditCard Model
        V Templates
        V URLs
    """
    databases = {"testsdb"}
    def setUp(self):
        # Setup variables for UserTests Class
        # Create client for tests
        self.client = Client()


    def test_creditcard_url_homepage(self):
        # Test : homepage URL is correct
        # Get the url of 'creditcardhome' view
        url = reverse('home')
        # Test -> url is as expected
        self.assertEqual("/", url)

    def test_creditcard_template_homepage(self):
        # Test : homepage template is correct
        # Get the url of 'home' view
        response = self.client.get(reverse('home'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == home.html (login) ?
        self.assertTemplateUsed(response, 'jkeys/home.html')
