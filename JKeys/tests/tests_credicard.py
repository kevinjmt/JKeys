from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from JKeys.models import CreditCard
from JKeys.forms import CreditCardForm


"""
LEGEND:
-> In each TestClass:
    V -> Tested
    ~ -> Partially Tested
    - -> Not Tested
"""




class CreditCardTests(TestCase):
    """
    Tests for CreditCard Model
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
        # Create CreditCard for testing (id=Kevin)
        CreditCard.objects.create(name="MyCard1", card_number="78942379487320473824324321", user_id=user1)
        CreditCard.objects.create(name="MyCard2", card_number="12312487937298047321412432", user_id=user1)
        CreditCard.objects.create(name="MyCard3", card_number="87980748328742331478216433", user_id=user1)
        # Create client for tests
        self.client = Client()

    def test_creditcard_model(self):
        # Tests : Model
        # Check CreditCard fields by saving them into variables
        MyCard1 = CreditCard.objects.get(name="MyCard1")
        MyCard2 = CreditCard.objects.get(name="MyCard2")
        MyCard3 = CreditCard.objects.get(name="MyCard3")
        # Tests -> Name Tests
        self.assertEqual('MyCard1', MyCard1.name)
        self.assertEqual('MyCard2', MyCard2.name)
        self.assertEqual('MyCard3', MyCard3.name)
        # Tests -> CardNumber Tests
        self.assertEqual('78942379487320473824324321', MyCard1.card_number)
        self.assertEqual('12312487937298047321412432', MyCard2.card_number)
        self.assertEqual('87980748328742331478216433', MyCard3.card_number)

    def test_creditcard_dynamic_form_create(self):
        # Tests (DYNAMIC) - FORMS : Create CreditCard using Forms
        # Create a CreditCard using the CreditCardForm to test if the form does work
        form = CreditCardForm(data={'name': 'MyCard4', 'card_number': '12312487937298047321412432'})
        # Now Save it by using the CreateCreditCard Form
        form.CreateCreditCard(User.objects.get(username="Mehdi"))
        # Test -> Check if all fields are correct
        self.assertEqual(form.data['name'], CreditCard.objects.get(name="MyCard4").name)
        self.assertEqual(form.data['card_number'], CreditCard.objects.get(name="MyCard4").card_number)

    def test_creditcard_dynamic_form_edit(self):
        # Tests (DYNAMIC) - FORMS : Edit CreditCard using Forms
        # Edit a CreditCard using the CreditCardForm to test if modifications have been saved successfully
        creditcard_to_edit = CreditCard.objects.get(name="MyCard1")
        form = CreditCardForm(data={'name': creditcard_to_edit.name, 'card_number': creditcard_to_edit.card_number})
        # Modify a field, here : name
        form.data["name"] = "caca"
        # Now Save it by using the EditLogin Form
        form.EditCreditCard(creditcard_to_edit)
        # Test -> Check if all fields are correct and modified
        self.assertEqual(form.data['name'], CreditCard.objects.get(card_number="78942379487320473824324321").name)
        self.assertEqual(form.data['card_number'], CreditCard.objects.get(card_number="78942379487320473824324321").card_number)

    def test_creditcard_dynamic_delete(self):
        # Tests (DYNAMIC) : Delete CreditCard using url
        todelete = CreditCard.objects.get(name="MyCard1")
        # URL generated to delete the item (get primary key to do so)
        url = reverse('deletecreditcard', kwargs={'pk': todelete.pk})
        # Confirm delete using URL
        self.client.delete(url)
        # Test -> Object does not exist anymore ?
        self.assertRaises(ObjectDoesNotExist, CreditCard.objects.get, name="MyCard1")



    def test_creditcard_access(self):
        # Test : Object can be accessed by another user ?
        # Filtering objects created by the user2
        user2_objects = CreditCard.objects.filter(user_id=2)
        # Test -> User2 have no items registered
        self.assertEqual(0, user2_objects.all().count())



    def test_creditcard_url_homepage(self):
        # Test : homepage URL is correct
        # Get the url of 'creditcardhome' view
        url = reverse('creditcardhome')
        # Test -> url is as expected
        self.assertEqual("/creditcards/", url)

    def test_creditcard_url_read(self):
        # Test : creditcardpage URL is correct
        # Get the object
        creditcard = CreditCard.objects.get(name="MyCard1")
        # Get the url of 'creditcardpage' view
        url = reverse('creditcardpage', kwargs={'pk': creditcard.pk})
        # Test -> url is as expected
        self.assertEqual("/creditcards/0", url)


    def test_creditcard_url_create(self):
        # Test : createcreditcard URL is correct
        # Get the url of 'createcreditcard' view
        url = reverse('createcreditcard')
        # Test -> url is as expected
        self.assertEqual("/creditcards/create", url)

    def test_creditcard_url_edit(self):
        # Test : editcreditcard URL is correct
        # Get the object
        creditcard = CreditCard.objects.get(name="MyCard1")
        # Get the url of 'editcreditcard' view
        url = reverse('editcreditcard', kwargs={'pk': creditcard.pk})
        # Test -> url is as expected
        self.assertEqual("/creditcards/0/edit", url)

    def test_creditcard_url_delete(self):
        # Test : deletecreditcard URL is correct
        # Get the object
        creditcard = CreditCard.objects.get(name="MyCard1")
        # Get the url of 'deletecreditcard' view
        url = reverse('deletecreditcard', kwargs={'pk': creditcard.pk})
        # Test -> url is as expected
        self.assertEqual("/creditcards/0/delete", url)




    def test_creditcard_template_homepage(self):
        # Test : homepage template is correct
        # Get the url of 'creditcardhome' view
        response = self.client.get(reverse('creditcardhome'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == home.html (login) ?
        self.assertTemplateUsed(response, 'jkeys/creditcard/home.html')

    def test_creditcard_template_createpage(self):
        # Test : createcreditcard template is correct
        # Create new user to load the page (can't be accessible without logging in)
        self.user = get_user_model().objects.create_user(username='Khaled', password='testpassword', email='test@example.com')
        # Get the url of 'createcreditcard' view
        response = self.client.get(reverse('createcreditcard'))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template gener9ated == createcreditcard.html ?
        self.assertTemplateUsed(response, 'jkeys/creditcard/createcreditcard.html')

    def test_creditcard_template_creditcardpage(self):
        # Test : creditcardpage template is correct
        # Get the object
        creditcard = CreditCard.objects.get(name="MyCard1")
        # Get the url of 'creditcardpage' view with creditcard id
        response = self.client.get(reverse('creditcardpage', args=(creditcard.id,)))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == creditcard.html ?
        self.assertTemplateUsed(response, 'jkeys/creditcard/creditcard.html')

    def test_creditcard_template_editpage(self):
        # Test : editcreditcard template is correct
        # Get the object
        self.user = get_user_model().objects.create_user(username='Khaled', password='testpassword', email='test@example.com')
        creditcard_to_edit = CreditCard.objects.get(name="MyCard1")
        # Get the url of 'editcreditcard' view with creditcard_to_edit id
        response = self.client.get(reverse('editcreditcard'), args=(creditcard_to_edit.id,))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == editcreditcard.html ?
        self.assertTemplateUsed(response, 'jkeys/creditcard/editcreditcard.html')

    def test_creditcard_template_deletepage(self):
        # Test : deletecreditcard template is correct
        # Get the object
        creditcard_to_delete = CreditCard.objects.get(name="MyCard1")
        # Get the url of 'deletecreditcard' view with creditcard_to_delete id
        response = self.client.get(reverse('deletecreditcard', args=(creditcard_to_delete.id,)))
        # Test -> Status code = 200 ? (HTML Code returned == 200 -> successfully generated)
        self.assertEqual(response.status_code, 200)
        # Test -> Template generated == deletecreditcard.html ?
        self.assertTemplateUsed(response, 'jkeys/creditcard/deletecreditcard.html')

