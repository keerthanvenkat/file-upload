from django import forms
from django.forms import ModelForm
from .models import Address

class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(required = True,widget = forms.Textarea)

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ['name','email','age']
