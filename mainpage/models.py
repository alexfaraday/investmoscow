from django.db import models
from django.contrib.auth.models import User


class Branch(models.Model):
    name = models.CharField(max_length=100)

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


class Order_Varibles(models.Model): #калькулятор
    industry_type = models.ForeignKey(Branch, on_delete=models.CASCADE)
    organisation_type = models.ForeignKey(company_type, on_delete=models.CASCADE)
    worker_amount = models.IntegerField(max_length=99999)
    area_type = models.CharField(max_length=100)
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

