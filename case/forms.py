from django import forms


class AnonymousForm(forms.Form):
    guid = forms.UUIDField(label='Nøgle')
