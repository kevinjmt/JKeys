from django.contrib import admin

from .models import Login, CreditCard, IdCard

# Register Id, CreditCard and IdCard models in admin panel
admin.site.register(Login)
admin.site.register(CreditCard)
admin.site.register(IdCard)