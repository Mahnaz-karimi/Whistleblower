from django import forms
from caseworker.models import Company


class AnonymousForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']
