from django.contrib import admin

from .models import Id, CreditCard, IdCard

# Register Id, CreditCard and IdCard models in admin panel
admin.site.register(Id)
admin.site.register(CreditCard)
admin.site.register(IdCard)