from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class create_user(UserCreationForm):
   first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
   last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
   email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
   phone_number = forms.CharField(max_length=13, required=True, help_text='Required')
   street_address = forms.CharField(max_length = 254, required=True, help_text='Required')

   class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'street_address')