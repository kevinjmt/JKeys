from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy, reverse

import JKeys.models
from JKeys.models import Login, IdCard, CreditCard
from JKeys.forms import LoginForm, IDCardForm, CreditCardForm

class LoginTests(TestCase):
    """
    Tests for Login Model
    """
    def setUp(self):
        """ Create Logins for testing """
        user1 = User.objects.create(username="Kevin")
        user2 = User.objects.create(username="Mehdi")
        Login.objects.create(name="Google", mail="testmail@mail.com", password="mypassword", link="https://google.com", user_id=user1)
        Login.objects.create(name="Microsoft", mail="testmail@mail.com", password="mspassword", link="https://microsoft.com", user_id=user1)
        Login.objects.create(name="GitHub", mail="testmail@mail.com", password="codeisopensource", link="https://github.com", user_id=user1)

    def test_login_read(self):
        """ Check Login fields """
        google = Login.objects.get(name="Google")
        microsoft = Login.objects.get(name="Microsoft")
        github = Login.objects.get(name="GitHub")

        # Name Tests
        self.assertEqual(google.name, 'Google')
        self.assertEqual(microsoft.name, 'Microsoft')
        self.assertEqual(github.name, 'GitHub')

        # Mail Tests
        self.assertEqual(google.mail, 'testmail@mail.com')
        self.assertEqual(microsoft.mail, 'testmail@mail.com')
        self.assertEqual(github.mail, 'testmail@mail.com')

        # Password Tests
        self.assertEqual(google.password, 'mypassword')
        self.assertEqual(microsoft.password, 'mspassword')
        self.assertEqual(github.password, 'codeisopensource')

        # Link Tests
        self.assertEqual(google.link, 'https://google.com')
        self.assertEqual(microsoft.link, 'https://microsoft.com')
        self.assertEqual(github.link, 'https://github.com')

    def test_login_dynamic_create(self):
        form = LoginForm(data={'name': 'StackOverflow', 'mail': 'mailfortest@mail.com', 'password': 'sopassword', 'link': 'https://stackoverflow.com'})
        form.CreateLogin(User.objects.get(username="Mehdi"))
        self.assertEqual(form.data['name'], Login.objects.get(name="StackOverflow").name)
        self.assertEqual(form.data['mail'], Login.objects.get(name="StackOverflow").mail)
        self.assertEqual(form.data['password'], Login.objects.get(name="StackOverflow").password)
        self.assertEqual(form.data['link'], Login.objects.get(name="StackOverflow").link)

    def test_login_dynamic_edit(self):
        modif = Login.objects.get(link="https://google.com")
        modif.name = "GoogleModified"
        modif.save()
        self.assertEqual(Login.objects.get(link="https://google.com").name, "GoogleModified")

    def test_login_dynamic_delete(self):
        todelete = Login.objects.get(link="https://google.com")
        todelete.delete()
        self.assertRaises(ObjectDoesNotExist, Login.objects.get, link="https://google.com")

    def test_login_access(self):
        user2_objects = Login.objects.filter(user_id=2)
        self.assertEqual(user2_objects.all().count(), 0)

    def test_login_template_homepage(self):
        login_homepage = self.client.get(reverse("loginhome"))
        self.assertTemplateUsed(login_homepage, "jkeys/login/home.html")

    def test_login_template_read(self):
        login_page = self.client.get(reverse("loginpage"))
        self.assertTemplateUsed(login_page, "jkeys/login/login.html")

    def test_login_template_create(self):
        login_createpage = self.client.get(reverse("loginpage"))
        self.assertTemplateUsed(login_createpage, "jkeys/login/createlogin.html")