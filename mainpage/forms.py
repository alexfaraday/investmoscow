from django import forms
from django.forms import ModelForm
from .models import Profile, Branch, Order_Varibles
from django.contrib.auth.models import User


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


class CalculatorForm(forms.ModelForm):
    class Meta:
        model = Order_Varibles
        fields = ['industry_type', 'organisation_type', 'worker_amount','area_type','area_is_special_economic','business_type','area_yardage','building_yardage','need_water',
                  'need_gas','need_electricity', 'is_patent_use']
        labels = {'industry_type':'Отрасль ведения хозяйственной деятельности',
                  'organisation_type':'Организационно-правовая форма',
        'worker_amount':'Количество сотрудников',
        'area_type':'Территория расположения производства',
        'area_is_special_economic':'Размещение в особой экономической зоне',
        'business_type':'Тип реализации проекта',
        'area_yardage':'Площадь производства',
        'building_yardage':'Площадь здания',
        'need_water':'Необходимо подключение к водопроводу',
                  'need_gas':'Необходимо подключение к газу',
        'need_electricity':'Необходимо подключение к электричеству',

        'is_patent_use':'Использовать патент' }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',

            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',

            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин',

            }),

        }