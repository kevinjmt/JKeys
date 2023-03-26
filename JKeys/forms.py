from django import forms
from .models import Login, IdCard, CreditCard
from django.utils import timezone

# Form for Login Model (needed to update fields in CreateView and EditView)
class LoginForm(forms.Form):
    # Fields to be filled in the login form connected to the model
    name = forms.CharField()
    mail = forms.CharField()
    password = forms.CharField()
    link = forms.CharField()

    # Fields to be modified in the database
    class Meta:
        model = Login
        fields = ['name', 'mail', 'password', 'link']

    # Fields to be filled in the CreateLogin form
    def CreateLogin(self, user):
        # Create a new login and connect fields named "name" or "password" in the html to the fields mentioned before
        new_login = Login(name=self.data.get("name"), mail=self.data.get("mail"),
                          password=self.data.get("password"), link=self.data.get("link"),
                          created=timezone.now(), modified=timezone.now(), user_id=user)
        # Once created, save it
        new_login.save()
        return new_login

    # Fields to be filled in the EditLogin form
    def EditLogin(self, login):
        # Edit the current login and connect fields named "name" or "password" in the html
        # to the current fields mentioned before of the current Login
        login.name = self.data.get("name")
        login.mail = self.data.get("mail")
        login.password = self.data.get("password")
        login.link = self.data.get("link")
        # Once modified, save it
        login.save()
        return login


# Form for IDCard Model (needed to update fields in CreateView and EditView)
class IDCardForm(forms.Form):
    # Fields to be filled in the idcard form connected to the model
    name = forms.CharField()
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()

    address1 = forms.CharField()
    address2 = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    postal_code = forms.CharField()
    country = forms.CharField()

    id_number = forms.CharField()

    # Fields to be modified in the database
    class Meta:
        model = IdCard
        fields = ['name', 'first_name', 'middle_name', 'last_name',
                  'address1', 'address2', 'city', 'state', 'postal_code', 'country',
                  'id_number']

    # Fields to be filled in the CreateIDCard form
    def CreateIdCard(self, user):
        # Create a new idcard and connect fields named "first_name" or "last_name" in the html
        # to the fields mentioned before
        new_id_card = IdCard(name=self.data.get("name"), first_name=self.data.get("first_name"),
                                 middle_name=self.data.get("middle_name"), last_name=self.data.get("last_name"),
                                 address1=self.data.get("address1"), address2=self.data.get("address2"),
                                 city=self.data.get("city"), state=self.data.get("state"),
                                 postal_code=self.data.get("postal_code"), country=self.data.get("country"),
                                 id_number=self.data.get("id_number"), created=timezone.now(), modified=timezone.now(),
                                 user_id=user)
        # Once created, save it
        new_id_card.save()
        return new_id_card

    # Fields to be filled in the EditIDCard form
    def EditIdCard(self, idcard):
        # Edit the current idcard and connect fields named "first_name" or "last_name" in the html
        # to the current fields mentioned before of the current idcard
        idcard.name = self.data.get("name")
        idcard.first_name = self.data.get("first_name")
        idcard.middle_name = self.data.get("middle_name")
        idcard.last_name = self.data.get("last_name")
        idcard.address1 = self.data.get("address1")
        idcard.address2 = self.data.get("address2")
        idcard.city = self.data.get("city")
        idcard.state = self.data.get("state")
        idcard.postal_code = self.data.get("postal_code")
        idcard.country = self.data.get("country")
        idcard.id_number = self.data.get("id_number")
        # Once modified, save it
        idcard.save()
        return idcard



# Form for CreditCard Model (needed to update fields in CreateView and EditView)
class CreditCardForm(forms.Form):
    # Fields to be filled in the creditcard form connected to the model
    name = forms.CharField()
    card_number = forms.CharField()

    # Fields to be modified in the database
    class Meta:
        model = CreditCard
        fields = ['name', 'card_number']

    # Fields to be filled in the CreateCreditCard form
    def CreateCreditCard(self, user):
        # Create a new creditcard and connect fields named "name" or "card_number" in the html
        # to the fields mentioned before
        new_credit_card = CreditCard(name=self.data.get("name"), card_number=self.data.get("card_number"),
                                     created=timezone.now(), modified=timezone.now(), user_id=user)
        # Once created, save it
        new_credit_card.save()
        return new_credit_card

    # Fields to be filled in the EditCreditCard form
    def EditCreditCard(self, creditcard):
        # Edit the current creditcard and connect fields named "name" or "card_number" in the html
        # to the current fields mentioned before of the current idcard
        creditcard.name = self.data.get("name")
        creditcard.card_number = self.data.get("card_number")
        # Once modified, save it
        creditcard.save()
        return creditcard