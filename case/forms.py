from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from caseworker.models import Address, Company


class CaseworkerAdmin(UserCreationForm):
    email = forms.EmailField()
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, related_name="address")
    company = models.ManyToManyField(Company)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
