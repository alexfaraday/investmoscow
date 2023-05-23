from django.db import models
from django.contrib.auth.models import User


class Branch(models.Model):
    name = models.CharField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, primary_key=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    branch = models.ManyToManyField(Branch, )
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Order_Varibles(models.Model):
    industry_type = models.CharField(max_length=100)
    organisation_type = models.CharField(max_length=100)
    worker_amount = models.IntegerField(max_length=99999)
    area_type=models.CharField(max_length=100)
    area_is_special_economic =models.BooleanField(default=False )
    business_type = models.ForeignKey(BusinessType, on_delete=models.CASCADE)
    area_yardage =models.IntegerField(max_length=999999)
    building_yardage =models.IntegerField(max_length=999999)
    need_water=models.BooleanField(default=False )
    need_gas=models.BooleanField(default=False )
    need_electricity=models.BooleanField(default=False )
    is_patent_use=models.BooleanField(default=False )


class BusinessType(models.Model):
    name=models.CharField(max_length=400)

class order_instruments(models.Model):
    instrument_name=models.CharField(max_length=100)
    instrument_amount=models.IntegerField(max_length=999999)
    instrument_price=models.IntegerField(max_length=999999)
    order=models.ForeignKey(Order_Varibles, on_delete=models.CASCADE)
