from django.db import models
from django.contrib.auth.models import User


class Branch(models.Model):
    name = models.CharField(max_length=100) #отрасль

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    organization = models.CharField(max_length=100)
    inn = models.CharField(max_length=100, blank=True)
    site = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


class BusinessType(models.Model): #Аренда/строительство
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name
class company_type(models.Model): #Организационно правовая форма
    type_name = models.CharField(max_length=100)
    def __str__(self):
        return self.type_name

class Moscow_zone(models.Model):
    name = models.CharField(max_length=100)#районы Москвы
    def __str__(self):
        return self.name


class Order_Varibles(models.Model): #калькулятор
    industry_type = models.ForeignKey(Branch, on_delete=models.CASCADE) #отрасль
    organisation_type = models.ForeignKey(company_type, on_delete=models.CASCADE) #ООПФ
    worker_amount = models.IntegerField(max_length=99999)# количество сотрудников
    area_type = models.ForeignKey(Moscow_zone, on_delete=models.CASCADE)  #район расположения
    area_is_special_economic = models.BooleanField(default=False )
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    area_yardage = models.IntegerField(max_length=999999)
    building_yardage = models.IntegerField(max_length=999999)
    need_water = models.BooleanField(default=False )
    need_gas = models.BooleanField(default=False )
    need_electricity = models.BooleanField(default=False )
    is_patent_use = models.BooleanField(default=False )



class order_instruments(models.Model): #Станок
    instrument_name = models.CharField(max_length=100)
    instrument_amount = models.IntegerField(max_length=999999)
    instrument_price = models.IntegerField(max_length=999999)
    order = models.ForeignKey(Order_Varibles, on_delete=models.CASCADE)

class CostCapitalConstraction(models.Model): #Стоимость капитального строительства
    min_CostCapitalConstraction = models.IntegerField(max_length=99999999)
    max_CostCapitalConstraction = models.IntegerField(max_length=99999999)


class Accounting(models.Model): #Бухгалтерский учет
    name = models.CharField(max_length=1000)
    min_osn = models.IntegerField(max_length=100000)
    max_osn = models.IntegerField(max_length=100000)
    min_usn = models.IntegerField(max_length=10000)
    max_usn = models.IntegerField(max_length=10000)
    min_patent = models.IntegerField(max_length=10000)
    max_patent = models.IntegerField(max_length=10000)

class StateDuty(models.Model): #Госпошлина
    name = models.CharField(max_length=1000)
    cost = models.IntegerField(max_length=1000)

class Industry(models.Model): #Обезличенные данные
    main_branch = models.CharField(max_length=1000)
    sub_branch = models.CharField(max_length=1000)
    average_number_staff = models.DecimalField(max_length=100)
    average_salary = models.DecimalField(max_length=100)
    taxes_to_budget = models.DecimalField(max_length=100)
    income_tax = models.DecimalField(max_length=100)
    property_tax = models.DecimalField(max_length=100)
    land_tax = models.DecimalField(max_length=100)
    ndfl = models.DecimalField(max_length=100)
    transport_tax = models.DecimalField(max_length=100)
    other_taxes = models.DecimalField(max_length=100)