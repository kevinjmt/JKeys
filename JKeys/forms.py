from django import forms
from .models import Login, IdCard, CreditCard
from django.utils import timezone

class LoginForm(forms.Form):
    name = forms.CharField()
    mail = forms.CharField()
    password = forms.CharField()
    link = forms.CharField()

    class Meta:
        model = Login
        fields = ['name', 'mail', 'password', 'link']

    def CreateLogin(self, user):
        new_login = Login(name=self.data.get("name"), mail=self.data.get("mail"),
                          password=self.data.get("password"), link=self.data.get("link"),
                          created=timezone.now(), modified=timezone.now(), user_id=user)
        new_login.save()
        return new_login

    def EditLogin(self, creditcard):
        creditcard.name = self.data.get("name")
        creditcard.mail = self.data.get("mail")
        creditcard.password = self.data.get("password")
        creditcard.link = self.data.get("link")
        creditcard.save()
        return creditcard


class IDCardForm(forms.Form):
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

    # Card or Passport Number
    id_number = forms.CharField()

    class Meta:
        model = IdCard
        fields = ['name', 'first_name', 'middle_name', 'last_name',
                  'address1', 'address2', 'city', 'state', 'postal_code', 'country',
                  'id_number']

    def CreateIdCard(self, user):
        new_id_card = IdCard(name=self.data.get("name"), first_name=self.data.get("first_name"),
                                 middle_name=self.data.get("middle_name"), last_name=self.data.get("last_name"),
                                 address1=self.data.get("address1"), address2=self.data.get("address2"),
                                 city=self.data.get("city"), state=self.data.get("state"),
                                 postal_code=self.data.get("postal_code"), country=self.data.get("country"),
                                 id_number=self.data.get("id_number"), created=timezone.now(), modified=timezone.now(), user_id=user)
        new_id_card.save()
        return new_id_card

    def EditIdCard(self, idcard):
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
        idcard.save()
        return idcard



class CreditCardForm(forms.Form):
    name = forms.CharField()
    card_number = forms.CharField()

    class Meta:
        model = CreditCard
        fields = ['name', 'card_number']

    def CreateCreditCard(self, user):
        new_credit_card = CreditCard(name=self.data.get("name"), card_number=self.data.get("card_number"), created=timezone.now(), modified=timezone.now(), user_id=user)
        new_credit_card.save()
        return new_credit_card

    def EditCreditCard(self, creditcard):
        creditcard.name = self.data.get("name")
        creditcard.card_number = self.data.get("card_number")
        creditcard.save()
        return creditcard