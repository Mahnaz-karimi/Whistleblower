from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from caseworker.models import Address, Company
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.shortcuts import redirect


class CaseworkerAdmin(UserCreationForm):
    email = forms.EmailField()
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, related_name="address")
    company = models.ManyToManyField(Company)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


'''
@receiver(post_save, sender=User)
def create_caseworker_profile(sender, instance, created, **kwargs):
    if created:
        CaseworkerAdmin.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_caseworker_profile(sender, instance, **kwargs):
    instance.profile.save()



def case_view(request):
    if (request.session['company_guid'] != 'valid'):
        return redirect('home_view')


case_context = {

    # ...

}
'''