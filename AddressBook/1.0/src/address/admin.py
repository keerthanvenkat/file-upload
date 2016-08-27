from django.contrib import admin

# Register your models here.
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    fields = ['email','name','age']

admin.site.register(Address, AddressAdmin)
