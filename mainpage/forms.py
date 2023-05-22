from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    organization = forms.CharField(max_length=100)
    site = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'surname', 'name',  'middle_name', 'email',
                  'organization', 'site', 'country', 'city', 'position', 'password1', 'password2', )