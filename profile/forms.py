from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    c_password = forms.CharField(widget=forms.PasswordInput) 

    class Meta:
        model = Customer
        fields = ['c_fullname', 'c_login_id', 'c_password', 'c_contact', 'c_email', 'c_address']
