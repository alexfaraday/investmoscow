from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, UpdateView, CreateView, DetailView, ListView
from .models import Profile, Order_Varibles
from .forms import ProfileForm,CalculatorForm,UserForm
from django import forms
from .pdf_maker import *
from .salary_function import *
from .accounting import *

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('mainpage:login')


class MainView(TemplateView):
    template_name = "mainpage/main.html"


class CalculationListView (ListView):
    model=Order_Varibles
    template_name = "mainpage/calculationlist.html"

class My_Oreder_CalculationListView (ListView):
    model=Order_Varibles
    template_name = "mainpage/my_calculationlist.html"

    def get_queryset(self):
        order = Order_Varibles.objects.filter(User_create_order=self.request.user)
        return order


class CalculatorView(CreateView):
    form_class = CalculatorForm

    template_name = "mainpage/calculator.html"
    success_url = '/'

    def form_valid(self, CalculatorForm):
        obj = CalculatorForm.save(commit=False)
        obj.User_create_order = self.request.user
       # salary_fss_pfr=wages(CalculatorForm.cleaned_data['industry_type'], CalculatorForm.cleaned_data['worker_amount'])
        salary_fss_pfr=wages(4, CalculatorForm.cleaned_data['worker_amount'])
        obj.pfr_min=salary_fss_pfr['6 месяцев']['ОПС']
        obj.oms_min=salary_fss_pfr['6 месяцев']['ОМС']
        obj.pfr_max=salary_fss_pfr['Год']['ОПС']
        obj.oms_max=salary_fss_pfr['Год']['ОПС']
        obj.vnim_min=salary_fss_pfr['6 месяцев']['ВНиМ']
        obj.vnim_max=salary_fss_pfr['Год']['ВНиМ']
        obj.ndfl_min=salary_fss_pfr['6 месяцев']['НДФЛ']
        obj.ndfl_max=salary_fss_pfr['Год']['НДФЛ']
        obj.salary_min=salary_fss_pfr['6 месяцев']['Зарплата']
        obj.salary_max=salary_fss_pfr['Год']['Зарплата']
        obj.total_personal_min=salary_fss_pfr['6 месяцев']['Итого']
        obj.total_personal_max=salary_fss_pfr['Год']['Итого']
        accunting= accounting_func(4,CalculatorForm.cleaned_data['worker_amount'])

        obj.total_AC6 =accunting[0]
        obj.total_AC15 =accunting[1]
        obj.total_AC_OSN =accunting[2]

        obj.excel_link =make_excel(CalculatorForm.cleaned_data['industry_type'],CalculatorForm.cleaned_data['organisation_type'],CalculatorForm.cleaned_data['worker_amount'],CalculatorForm.cleaned_data['area_type'], salary_fss_pfr)




        obj.save()

        newpage=Order_Varibles.objects.filter(User_create_order=self.request.user).last()

        return redirect("/calculation/"+str(newpage.id))



class CalculationDetailView(DetailView):
    model = Order_Varibles
    template_name = "mainpage/one_caluclation.html"


def registration(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = ProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            # получаем имя пользователя и пароль из формы
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password1')
            name = form2.cleaned_data.get('name')
            surname = form2.cleaned_data.get('surname')
            middle_name = form2.cleaned_data.get('middle_name')
            email = form2.cleaned_data.get('email')
            organization = form2.cleaned_data.get('organization')
            inn = form2.cleaned_data.get('inn')
            site = form2.cleaned_data.get('site')
            branch = form2.cleaned_data.get('branch')
            country = form2.cleaned_data.get('country')
            city = form2.cleaned_data.get('city')
            position = form2.cleaned_data.get('position')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            Profile.objects.create(user=request.user, name=name, surname=surname, middle_name=middle_name,
                                   email=email, organization=organization, inn=inn, site=site, branch=branch,
                                   country=country, city=city, position=position)
            return render(request, 'mainpage/main.html')
    else:
        form1 = UserCreationForm()
        form2 = ProfileForm()
    return render(request, 'mainpage/register.html', {'form1': form1, 'form2': form2})


class ProfileDetailView(View):
    def get(self, request: HttpRequest, ) -> HttpResponse:
        profile = Profile.objects.get(user=request.user)
        context = {
            "profile": profile
        }
        return render(request, 'mainpage/profile.html', context=context)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = '/'
    pk_url_kwarg = "oid"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            userid = Profile.objects.get(id=self.kwargs["oid"])
            if request.user.id != userid.userid:
                return HttpResponseRedirect("/")
            return super().get(request, *args, **kwargs)
        else:
            return redirect("/")

    def form_valid(self, form: forms.Form):
        if form.is_valid():
            return super(ProfileUpdateView, self).form_valid(form)
        return self.form_invalid(form)


    #def get_success_url(self):
     #   return reverse('mainpage:profile', kwargs={'pk': self.object.id})



def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('/profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    useratr = Profile.objects.all().filter(user=request.user)
    return render(request, 'mainpage/profile_form.html', {
        #'user_form': user_form,
        'profile_form': profile_form,

        "useratr": useratr
    })
