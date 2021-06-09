from django.contrib import admin
from caseworker.models import Country, PostalCode, Company, Address


admin.site.register(PostalCode)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Country)
