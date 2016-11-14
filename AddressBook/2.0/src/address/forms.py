from django import forms
from .models import Address




class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'age', 'email']

    # todo : Meta

    def clean_email(self):
        email = self.cleaned_data.get('email') # student3@gmail.com
        (ename,edomain) = email.split('@')
        if edomain != 'edu.com':
            raise forms.ValidationError("Please make sure your email address is edu.com")
        else:
            return email

    def clean_age(self):
        age = self.cleaned_data.get('age') # 21
        if age > 18 and age < 50:
            return age
        else:
            raise forms.ValidationError("Buddy!! you are still a kiddo at {}".format(age))
