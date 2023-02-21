from django.contrib import admin

from .models import Id, CreditCard, IdCard

admin.site.register(Id)
admin.site.register(CreditCard)
admin.site.register(IdCard)