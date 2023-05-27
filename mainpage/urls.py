from django.contrib.auth.views import LoginView
from django.urls import path
from .views import MyLogoutView, MainView, CalculatorView, registration, ProfileDetailView, ProfileUpdateView
from mainpage import views


app_name = "mainpage"
urlpatterns = [
    path('', registration, name="register"),
    path('calculator/', CalculatorView.as_view(), name="calculator"),
    #path('main/<int:pk>/update/', ProfileUpdateView.as_view(), name="profile_update"),
    path('editprofile/', views.update_profile),
   # path('main/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
    path('profile/', ProfileDetailView.as_view(), name="profile"),

    path('logout/', MyLogoutView.as_view(), name="logout"),
    path("login/",
         LoginView.as_view(
             template_name="mainpage/login.html",


         ),
         name="login"),
    path('main/', MainView.as_view(), name="main"),
    ]
