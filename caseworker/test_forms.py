from django.test import TestCase
from caseworker.forms import CaseworkerAdmin
from caseworker.models import Company, Country, PostalCode, Address


class TestForms(TestCase):

    def test_CaseworkerAdmin_form(self):
        form = CaseworkerAdmin(data={
            'username': 'Mahn',
            'first_name': 'Test123',
            'last_name': 'Test123',
            'password1':'test123',
            'password2': 'test123',
            'email': 'mahnaazi@yahoo.com',

        })
        print("helllllloo", CaseworkerAdmin)
        self.assertFalse(form.is_valid())

    def test_CaseworkerAdmin_no_data(self):
        form = CaseworkerAdmin(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

