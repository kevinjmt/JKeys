from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils import timezone

from JKeys.models import IdCard
from JKeys.forms import IDCardForm


"""
LEGEND:
-> In each TestClass:
    V -> Tested
    ~ -> Partially Tested
    - -> Not Tested
"""


class IdCardTests(TestCase):
    """
    Tests for IdCard Model
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
        # Create IdCard for testing (id=Kevin)
        IdCard.objects.create(name="Kevin", first_name="Kevin",
                                 middle_name="Kevin", last_name="JAMET",
                                 address1="Address1", address2="Address2",
                                 city="City", state="State",
                                 postal_code="8490284", country="France",
                                 id_number="7849327480723197480327147302", created=timezone.now(), modified=timezone.now(),
                                 user_id=user1)
        IdCard.objects.create(name="John", first_name="John",
                                 middle_name="John", last_name="TestName",
                                 address1="Address1", address2="Address2",
                                 city="City2", state="State2",
                                 postal_code="47839270", country="Ireland",
                                 id_number="1213261478369246302123432", created=timezone.now(), modified=timezone.now(),
                                 user_id=user1)
        # Create client for tests
        self.client = Client()

    def test_idcard_model(self):
        # Tests : Model
        # Check IdCard fields by saving them into variables
        id1 = IdCard.objects.get(name="Kevin")
        id2 = IdCard.objects.get(name="John")
        # Tests -> Name Tests
        self.assertEqual('Kevin', id1.name)
        self.assertEqual('John', id2.name)
        # Tests -> FirstName Tests
        self.assertEqual('Kevin', id1.first_name)
        self.assertEqual('John', id2.first_name)
        # Tests -> MiddleName Tests
        self.assertEqual('Kevin', id1.middle_name)
        self.assertEqual('John', id2.middle_name)
        # Tests -> LastName Tests
        self.assertEqual('JAMET', id1.last_name)
        self.assertEqual('TestName', id2.last_name)
        # Tests -> Address1 Tests
        self.assertEqual('Address1', id1.address1)
        self.assertEqual('Address1', id2.address1)
        # Tests -> Address2 Tests
        self.assertEqual('Address2', id1.address2)
        self.assertEqual('Address2', id2.address2)
        # Tests -> City Tests
        self.assertEqual('City', id1.city)
        self.assertEqual('City2', id2.city)
        # Tests -> State Tests
        self.assertEqual('State', id1.state)
        self.assertEqual('State2', id2.state)
        # Tests -> PostalCode Tests
        self.assertEqual('8490284', id1.postal_code)
        self.assertEqual('47839270', id2.postal_code)
        # Tests -> Country Tests
        self.assertEqual('France', id1.country)
        self.assertEqual('Ireland', id2.country)
        # Tests -> idNumber Tests
        self.assertEqual('7849327480723197480327147302', id1.id_number)
        self.assertEqual('1213261478369246302123432', id2.id_number)

    def test_idcard_dynamic_form_create(self):
        # Tests (DYNAMIC) - FORMS : Create IdCard using Forms
        # Create a IdCard using the IDCardForm to test if the form does work
        form = IDCardForm(data={'name':"John1", 'first_name':"John",
                                 'middle_name':"John", 'last_name':"TestName",
                                 'address1':"Address1", 'address2':"Address2",
                                 'city':"City2", 'state':"State2",
                                 'postal_code':"47839270", 'country':"Ireland",
                                 'id_number':"1213261478369246302123432"})
        # Now Save it by using the CreateIdCard Form
        form.CreateIdCard(User.objects.get(username="Mehdi"))
        # Test -> Check if all fields are correct
        self.assertEqual(form.data['name'], IdCard.objects.get(name="John1").name)
        self.assertEqual(form.data['first_name'], IdCard.objects.get(name="John1").first_name)
        self.assertEqual(form.data['middle_name'], IdCard.objects.get(name="John1").middle_name)
        self.assertEqual(form.data['last_name'], IdCard.objects.get(name="John1").last_name)
        self.assertEqual(form.data['address1'], IdCard.objects.get(name="John1").address1)
        self.assertEqual(form.data['address2'], IdCard.objects.get(name="John1").address2)
        self.assertEqual(form.data['city'], IdCard.objects.get(name="John1").city)
        self.assertEqual(form.data['state'], IdCard.objects.get(name="John1").state)
        self.assertEqual(form.data['postal_code'], IdCard.objects.get(name="John1").postal_code)
        self.assertEqual(form.data['country'], IdCard.objects.get(name="John1").country)
        self.assertEqual(form.data['id_number'], IdCard.objects.get(name="John1").id_number)

    def test_idcard_dynamic_form_edit(self):
        # Tests (DYNAMIC) - FORMS : Edit IdCard using Forms
        # Edit a IdCard using the IDCardForm to test if modifications have been saved successfully
        idcard_to_edit = IdCard.objects.get(name="John")
        form = IDCardForm(data={'name': idcard_to_edit.name, 'first_name': idcard_to_edit.first_name,
                                 'middle_name': idcard_to_edit.middle_name, 'last_name': idcard_to_edit.last_name,
                                 'address1': idcard_to_edit.address1, 'address2': idcard_to_edit.address2,
                                 'city': idcard_to_edit.city, 'state': idcard_to_edit.state,
                                 'postal_code': idcard_to_edit.postal_code, 'country': idcard_to_edit.country,
                                 'id_number': idcard_to_edit.id_number})
        # Modify a field, here : name
        form.data["name"] = "caca"
        # Now Save it by using the EditIdCard Form
        form.EditIdCard(idcard_to_edit)
        # Test -> Check if all fields are correct and modified
        self.assertEqual(form.data['name'], IdCard.objects.get(first_name="John").name)
        self.assertEqual(form.data['first_name'], IdCard.objects.get(first_name="John").first_name)
        self.assertEqual(form.data['middle_name'], IdCard.objects.get(first_name="John").middle_name)
        self.assertEqual(form.data['last_name'], IdCard.objects.get(first_name="John").last_name)
        self.assertEqual(form.data['address1'], IdCard.objects.get(first_name="John").address1)
        self.assertEqual(form.data['address2'], IdCard.objects.get(first_name="John").address2)
        self.assertEqual(form.data['city'], IdCard.objects.get(first_name="John").city)
        self.assertEqual(form.data['state'], IdCard.objects.get(first_name="John").state)
        self.assertEqual(form.data['postal_code'], IdCard.objects.get(first_name="John").postal_code)
        self.assertEqual(form.data['country'], IdCard.objects.get(first_name="John").country)
        self.assertEqual(form.data['id_number'], IdCard.objects.get(first_name="John").id_number)

    def test_idcard_dynamic_delete(self):
        # Tests (DYNAMIC) : Delete IdCard using url
        todelete = IdCard.objects.get(name="John")
        # URL generated to delete the item (get primary key to do so)
        url = reverse('deleteidcard', kwargs={'pk': todelete.pk})
        # Confirm delete using URL
        self.client.delete(url)
        # Test -> Object does not exist anymore ?
        self.assertRaises(ObjectDoesNotExist, IdCard.objects.get, name="John")



    def test_idcard_access(self):
        # Test : Object can be accessed by another user ?
        # Filtering objects created by the user2
        user2_objects = IdCard.objects.filter(user_id=2)
        # Test -> User2 have no items registered
        self.assertEqual(0, user2_objects.all().count())



    def test_idcard_url_homepage(self):
        # Test : homepage URL is correct
        # Get the url of 'idcardhome' view
        url = reverse('idcardhome')
        # Test -> url is as expected
        self.assertEqual("/idcards/", url)

    def test_idcard_url_read(self):
        # Test : idcardpage URL is correct
        # Get the object
        login = IdCard.objects.get(name="John")
        # Get the url of 'idcardpage' view
        url = reverse('idcardpage', kwargs={'pk': login.pk})
        # Test -> url is as expected
        self.assertEqual("/idcards/0", url)


    def test_idcard_url_create(self):
        # Test : createidcard URL is correct
        # Get the url of 'createidcard' view
        url = reverse('createidcard')
        # Test -> url is as expected
        self.assertEqual("/idcards/create", url)

    def test_idcard_url_edit(self):
        # Test : editidcard URL is correct
        # Get the object
        login = IdCard.objects.get(name="John")
        # Get the url of 'editidcard' view
        url = reverse('editidcard', kwargs={'pk': login.pk})
        # Test -> url is as expected
        self.assertEqual("/idcards/0/edit", url)

    def test_idcard_url_delete(self):
        # Test : deleteidcard URL is correct
        # Get the object
        login = IdCard.objects.get(name="John")
        # Get the url of 'deleteidcard' view
        url = reverse('deleteidcard', kwargs={'pk': login.pk})
        # Test -> url is as expected
        self.assertEqual("/idcards/0/delete", url)




    def test_idcard_template_homepage(self):
        # Test : homepage template is correct
        # Get the url of 'idcardhome' view
        response = self.client.get(reverse('idcardhome'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == home.html (login) ?
        self.assertTemplateUsed(response, 'jkeys/idcard/home.html')

    def test_idcard_template_createpage(self):
        # Test : createidcard template is correct
        # Create new user to load the page (can't be accessible without logging in)
        self.user = get_user_model().objects.create_user(username='Khaled', password='testpassword', email='test@example.com')
        # Get the url of 'createidcard' view
        response = self.client.get(reverse('createidcard'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == createidcard.html ?
        self.assertTemplateUsed(response, 'jkeys/idcard/createidcard.html')

    def test_idcard_template_idcardpage(self):
        # Test : idcardpage template is correct
        # Get the object
        idcard = IdCard.objects.get(name="John")
        # Get the url of 'idcardpage' view with idcard id
        response = self.client.get(reverse('idcardpage', args=(idcard.id,)))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == idcard.html ?
        self.assertTemplateUsed(response, 'jkeys/idcard/idcard.html')

    def test_idcard_template_editpage(self):
        # Test : editidcard template is correct
        # Get the object
        self.user = get_user_model().objects.create_user(username='Khaled', password='testpassword', email='test@example.com')
        idcard_to_edit = IdCard.objects.get(name="John")
        # Get the url of 'editidcard' view with idcard_to_edit id
        response = self.client.get(reverse('editidcard'), args=(idcard_to_edit.id,))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == editidcard.html ?
        self.assertTemplateUsed(response, 'jkeys/idcard/editidcard.html')

    def test_idcard_template_deletepage(self):
        # Test : deleteidcard template is correct
        # Get the object
        idcard_to_delete = IdCard.objects.get(name="John")
        # Get the url of 'deleteidcard' view with idcard_to_delete id
        response = self.client.get(reverse('deleteidcard', args=(idcard_to_delete.id,)))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == deleteidcard.html ?
        self.assertTemplateUsed(response, 'jkeys/idcard/deleteidcard.html')


