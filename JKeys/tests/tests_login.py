from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from JKeys.models import Login
from JKeys.forms import LoginForm


"""
LEGEND:
-> In each TestClass:
    V -> Tested
    ~ -> Partially Tested
    - -> Not Tested
"""


class LoginTests(TestCase):
    """
    Tests for Login Model
        V Models
        V User Foreign Key
        V Forms
        V Templates
        V URLs
    """
    databases = {"testsdb"}
    def setUp(self):
        # Setup variables for UserTests Class
        # Create users to test ownership
        user1 = User.objects.create(username="Kevin", password="test1")
        user2 = User.objects.create(username="Mehdi", password="test2")
        # Create Logins for testing (id=Kevin)
        Login.objects.create(name="Google", mail="testmail@mail.com", password="mypassword", link="https://google.com", user_id=user1)
        Login.objects.create(name="Microsoft", mail="testmail@mail.com", password="mspassword", link="https://microsoft.com", user_id=user1)
        Login.objects.create(name="GitHub", mail="testmail@mail.com", password="codeisopensource", link="https://github.com", user_id=user1)
        # Create client for tests
        self.client = Client()

    def test_login_model(self):
        # Tests : Model
        # Check Login fields by saving them into variables
        google = Login.objects.get(name="Google")
        microsoft = Login.objects.get(name="Microsoft")
        github = Login.objects.get(name="GitHub")
        # Tests -> Name Tests
        self.assertEqual('Google', google.name)
        self.assertEqual('Microsoft', microsoft.name)
        self.assertEqual('GitHub', github.name)
        # Tests -> Mail Tests
        self.assertEqual('testmail@mail.com', google.mail)
        self.assertEqual('testmail@mail.com', microsoft.mail)
        self.assertEqual('testmail@mail.com', github.mail)
        # Tests -> Password Tests
        self.assertEqual('mypassword', google.password)
        self.assertEqual('mspassword', microsoft.password)
        self.assertEqual('codeisopensource', github.password)
        # Tests -> Link Tests
        self.assertEqual('https://google.com', google.link)
        self.assertEqual('https://microsoft.com', microsoft.link)
        self.assertEqual('https://github.com', github.link)

    def test_login_dynamic_form_create(self):
        # Tests (DYNAMIC) - FORMS : Create Login using Forms
        # Create a Login using the LoginForm to test if the form does work
        form = LoginForm(data={'name': 'StackOverflow', 'mail': 'mailfortest@mail.com', 'password': 'sopassword', 'link': 'https://stackoverflow.com'})
        # Now Save it by using the CreateLogin Form
        form.CreateLogin(User.objects.get(username="Mehdi"))
        # Test -> Check if all fields are correct
        self.assertEqual(form.data['name'], Login.objects.get(name="StackOverflow").name)
        self.assertEqual(form.data['mail'], Login.objects.get(name="StackOverflow").mail)
        self.assertEqual(form.data['password'], Login.objects.get(name="StackOverflow").password)
        self.assertEqual(form.data['link'], Login.objects.get(name="StackOverflow").link)

    def test_login_dynamic_form_edit(self):
        # Tests (DYNAMIC) - FORMS : Edit Login using Forms
        # Edit a Login using the LoginForm to test if modifications have been saved successfully
        login_to_edit = Login.objects.get(link="https://google.com")
        form = LoginForm(data={'name': login_to_edit.name, 'mail': login_to_edit.mail, 'password': login_to_edit.password, 'link': login_to_edit.link})
        # Modify a field, here : name
        form.data["name"] = "caca"
        # Now Save it by using the EditLogin Form
        form.EditLogin(login_to_edit)
        # Test -> Check if all fields are correct and modified
        self.assertEqual(form.data['name'], Login.objects.get(link="https://google.com").name)
        self.assertEqual(form.data['mail'], Login.objects.get(link="https://google.com").mail)
        self.assertEqual(form.data['password'], Login.objects.get(link="https://google.com").password)
        self.assertEqual(form.data['link'], Login.objects.get(link="https://google.com").link)

    def test_login_dynamic_delete(self):
        # Tests (DYNAMIC) : Delete Login using url
        todelete = Login.objects.get(link="https://google.com")
        # URL generated to delete the item (get primary key to do so)
        url = reverse('deletelogin', kwargs={'pk': todelete.pk})
        # Confirm delete using URL
        self.client.delete(url)
        # Test -> Object does not exist anymore ?
        self.assertRaises(ObjectDoesNotExist, Login.objects.get, link="https://google.com")



    def test_login_access(self):
        # Test : Object can be accessed by another user ?
        # Filtering objects created by the user2
        user2_objects = Login.objects.filter(user_id=2)
        # Test -> User2 have no items registered
        self.assertEqual(0, user2_objects.all().count())



    def test_login_url_homepage(self):
        # Test : homepage URL is correct
        # Get the url of 'loginhome' view
        url = reverse('loginhome')
        # Test -> url is as expected
        self.assertEqual("/logins/", url)

    def test_login_url_read(self):
        # Test : loginpage URL is correct
        # Get the object
        login = Login.objects.get(link="https://google.com")
        # Get the url of 'loginpage' view
        url = reverse('loginpage', kwargs={'pk': login.pk})
        # Test -> url is as expected
        self.assertEqual("/logins/0", url)


    def test_login_url_create(self):
        # Test : createlogin URL is correct
        # Get the url of 'createlogin' view
        url = reverse('createlogin')
        # Test -> url is as expected
        self.assertEqual("/logins/create", url)

    def test_login_url_edit(self):
        # Test : editlogin URL is correct
        # Get the object
        login = Login.objects.get(link="https://google.com")
        # Get the url of 'editlogin' view
        url = reverse('editlogin', kwargs={'pk': login.pk})
        # Test -> url is as expected
        self.assertEqual("/logins/0/edit", url)

    def test_login_url_delete(self):
        # Test : deletelogin URL is correct
        # Get the object
        login = Login.objects.get(link="https://google.com")
        # Get the url of 'deletelogin' view
        url = reverse('deletelogin', kwargs={'pk': login.pk})
        # Test -> url is as expected
        self.assertEqual("/logins/0/delete", url)




    def test_login_template_homepage(self):
        # Test : homepage template is correct
        # Get the url of 'loginhome' view
        response = self.client.get(reverse('loginhome'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == home.html (login) ?
        self.assertTemplateUsed(response, 'jkeys/login/home.html')

    def test_login_template_createpage(self):
        # Test : createlogin template is correct
        # Create new user to load the page (can't be accessible without logging in)
        self.user = get_user_model().objects.create_user(username='Khaled', password='testpassword', email='test@example.com')
        # Get the url of 'createlogin' view
        response = self.client.get(reverse('createlogin'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == createlogin.html ?
        self.assertTemplateUsed(response, 'jkeys/login/createlogin.html')

    def test_login_template_loginpage(self):
        # Test : loginpage template is correct
        # Get the object
        login = Login.objects.get(link="https://google.com")
        # Get the url of 'loginpage' view with login id
        response = self.client.get(reverse('loginpage', args=(login.id,)))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == login.html ?
        self.assertTemplateUsed(response, 'jkeys/login/login.html')

    def test_login_template_editpage(self):
        # Test : editlogin template is correct
        # Get the object
        self.user = get_user_model().objects.create_user(username='Khaled', password='testpassword', email='test@example.com')
        login_to_edit = Login.objects.get(link="https://google.com")
        # Get the url of 'editlogin' view with login_to_edit id
        response = self.client.get(reverse('editlogin'), args=(login_to_edit.id,))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == editlogin.html ?
        self.assertTemplateUsed(response, 'jkeys/login/editlogin.html')

    def test_login_template_deletepage(self):
        # Test : deletelogin template is correct
        # Get the object
        login_to_delete = Login.objects.get(link="https://google.com")
        # Get the url of 'deletelogin' view with login_to_delete id
        response = self.client.get(reverse('deletelogin', args=(login_to_delete.id,)))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == deletelogin.html ?
        self.assertTemplateUsed(response, 'jkeys/login/deletelogin.html')
