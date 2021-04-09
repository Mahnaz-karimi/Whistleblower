from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import uuid


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PostalCode(models.Model):
    post_code = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country")

    def __str__(self):  # return the name we will object calls
        return self.city_name


class Address(models.Model):
    street = models.CharField(max_length=255)
    post_code = models.ForeignKey(PostalCode, on_delete=models.CASCADE, related_name="postalcode")

    def __str__(self):
        return self.street


class Company(models.Model):
    name = models.CharField(max_length=255)
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="address")

    def __str__(self):
        return self.name


class CaseworkerAdmin(UserCreationForm):
    email = forms.EmailField()
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, related_name="address")
    company = models.ManyToManyField(Company)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
