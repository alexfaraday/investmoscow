from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import registration, ProfileView, MyLogoutView, MainView, CalculatorView


app_name = "mainpage"
urlpatterns = [
    path('register/', registration, name="register"),
    path('main/profile/', ProfileView.as_view(), name="profile"),
    path('logout/', MyLogoutView.as_view(), name="logout"),
    path("",
         LoginView.as_view(
             template_name="mainpage/login.html",
             redirect_authenticated_user=True,

         ),
         name="login"),
    path('main/', MainView.as_view(), name="main"),
    path('main/calculator/', CalculatorView.as_view(), name="calculator")
]
