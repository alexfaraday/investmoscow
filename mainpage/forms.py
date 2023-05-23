from django import forms
from django.forms import ModelForm
from .models import Profile, Branch


class ProfileForm(ModelForm):
    surname = forms.CharField(label='Фамилия', max_length=100)
    name = forms.CharField(label='Имя', max_length=100)
    middle_name = forms.CharField(label='Отчество', max_length=100)
    email = forms.EmailField(label='Почта', max_length=100)
    organization = forms.CharField(label='Название организации', max_length=100)
    inn = forms.CharField(label='ИНН', max_length=100)
    site = forms.CharField(label="Веб-сайт организации", max_length=100)
    branch = forms.ModelChoiceField(label="Отрасль ведения хозяйственной деятельности", queryset=Branch.objects.all(),
                                    empty_label="")
    country = forms.CharField(label='Страна', max_length=100)
    city = forms.CharField(label='Город', max_length=100)
    position = forms.CharField(label='Должность', max_length=100)

    class Meta:
        model = Profile
        fields = ['surname', 'name', 'middle_name', 'email', 'organization', 'inn',
                  'site', 'branch', 'country', 'city', 'position']
