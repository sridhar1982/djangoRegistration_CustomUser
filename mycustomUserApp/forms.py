from registration.forms import RegistrationForm
from django import forms


class MyRegistrationForm(RegistrationForm):
    age = forms.CharField(required=False)