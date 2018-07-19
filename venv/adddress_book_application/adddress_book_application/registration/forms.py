from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateContactForm(UserCreationForm):
    first_name = forms.TextInput(help_text='Required')
    last_name = forms.TextInput(help_text='Required')
    email = forms.EmailField(help_text='Required')
    phone_number = forms.TextInput(help_text="Required")
    street_address = forms.TextInput(help_text="Required")

    class Meta:
        mordel = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'street_address', 'password')

