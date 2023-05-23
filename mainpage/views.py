from django.contrib.auth.views import LogoutView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView
from .models import Profile
from .forms import SignUpForm
from .models import Order_Varibles


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('mainpage:login')


class ProfileView(TemplateView):
    template_name = "mainpage/profile.html"


class MainView(TemplateView):
    template_name = "mainpage/main.html"


class CalculatorView(CreateView):
    model = Order_Varibles
    fields = '__all__'
    template_name = "mainpage/calculator.html"
    success_url = '/'


def registration(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user,
                                   name=form.cleaned_data.get('name'),
                                   surname=form.cleaned_data.get('surname'),
                                   middle_name=form.cleaned_data.get('middle_name'),
                                   email=form.cleaned_data.get('email'),
                                   organization=form.cleaned_data.get('organization'),
                                   site=form.cleaned_data.get('site'),
                                   country=form.cleaned_data.get('country'),
                                   city=form.cleaned_data.get('city'),
                                   position=form.cleaned_data.get('position')
                                   )
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, 'mainpage/main.html')
    else:
        form = SignUpForm()
    return render(request, 'mainpage/register.html', {'form': form})