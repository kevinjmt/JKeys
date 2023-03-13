from datetime import timezone
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django import forms


"""
class Profile(models.Model):
    name = models.CharField(max_length=200)
"""

# Class for Login model
class Login(models.Model):
    # Attributes in database to put in Text Fields
    # Char Fields for all attributes in this part with default='' and maxlength of 200 chars
    name = models.CharField(max_length=200, default="")
    mail = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")  # TO ENCRYPT
    link = models.CharField(max_length=200, default="")

    # Fields for Creation and Modification Dates
    # Created -> editable=false to do not modify this date
    # Modified -> auto_now=true to be changed automatically
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(auto_now=True)

    # Connect to the User who created the Login as a ForeignKey
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Save function to save Creation and Modification Date
    def save(self, *args, **kwargs):
        ''' On save, update modification date and creation date '''
        # If the element is not yet created -> change creation date to now
        # In every situation, when saved, change modification date to now
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        # Override and give to model new arguments
        return super(Login, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



# Class for CreditCard model
class CreditCard(models.Model):
    # Attributes in database to put in Text Fields
    # Char Fields for all attributes in this part with default='' and maxlength of 200 chars
    # Not storing the CVV (Card Validation Value) because of privacy purposes
    name = models.CharField(max_length=200, default="")
    card_number = models.CharField(max_length=200, default="")

    # Connect to the User who created the CreditCard as a ForeignKey
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Fields for Creation and Modification Dates
    # Created -> editable=false to do not modify this date
    # Modified -> auto_now=true to be changed automatically
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update modification date and creation date '''
        # If the element is not yet created -> change creation date to now
        # In every situation, when saved, change modification date to now
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        # Override and give to model new arguments
        return super(CreditCard, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



# Class for IdCard model
class IdCard(models.Model):
    # Attributes in database to put in Text Fields
    # Char Fields for all attributes in this part with default='' and maxlength of 200 chars
    name = models.CharField(max_length=200, default="")
    first_name = models.CharField(max_length=200, default="")
    middle_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")

    address1 = models.CharField(max_length=200, default="")
    address2 = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    postal_code = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")

    # IDCard or Passport Number
    id_number = models.CharField(max_length=250, default="")

    # Connect to the User who created the IDCard as a ForeignKey
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



    # Fields for Creation and Modification Dates
    # Created -> editable=false to do not modify this date
    # Modified -> auto_now=true to be changed automatically
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update modification date and creation date '''
        # If the element is not yet created -> change creation date to now
        # In every situation, when saved, change modification date to now
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        # Override and give to model new arguments
        return super(IdCard, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
