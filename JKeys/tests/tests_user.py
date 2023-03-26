from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail



"""
LEGEND:
-> In each TestClass:
    V -> Tested
    ~ -> Partially Tested
    - -> Not Tested
"""

class UserTests(TestCase):
    """
    Tests for User Authentication
        V Log In
        V Sign Up
        ~ Templates
        - URLs
        V Emails
    """
    databases = {"testsdb"}
    def setUp(self):
        # Setup variables for UserTests Class
        # Sign Up User by creating it
        self.user = get_user_model().objects.create_user(username='Kevin', password='testpassword', email='test@example.com')
        self.user.save()

    def test_user_authentication(self):
        # Test if user is authenticated (Log In)
        user = authenticate(username='Kevin', password='testpassword')
        # Test -> User logged in successfully ?
        self.assertTrue((user is not None) and user.is_authenticated)


    def test_user_wrong_authentication(self):
        # Test if user is authenticated (Log In)
        # Using wrong IDs -> not able to connect
        user = authenticate(username='wrong', password='testpasswordwrong')
        # Test -> User logged in successfully ? (using wrong IDs) -> FALSE
        self.assertFalse(user is not None and user.is_authenticated)


    def test_user_send_reset_password_email(self):
        # Send message reset password mail.
        mail.send_mail(
            "Reset Password",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )

        # Test that one message has been sent.
        # Test -> Mail generated ?
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        # Test -> Last email (just sent) subject == 'Reset Password' ?
        self.assertEqual(mail.outbox[0].subject, "Reset Password")

    def test_user_template_signup(self):
        # Test Signup Template
        # Create client to generate template
        client = Client()
        # Save template generated using the client
        response = client.get(reverse('signup'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == signup.html ?
        self.assertTemplateUsed(response, 'registration/signup.html')
