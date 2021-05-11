from django.test import TestCase
from caseworker.forms import CaseworkerAdmin
# from caseworker.models import Company, Country, PostalCode, Address


class TestForms(TestCase):

    def test_CaseworkerAdmin_form_true(self):
        form = CaseworkerAdmin(data={
            'username': 'Mahn',
            'password1': 'madrese122',
            'password2': 'madrese122',
            'email': 'mahnaazi@yahoo.com'

        })
        # print("print form : ", form)
        self.assertTrue(form.is_valid())

    def test_CaseworkerAdmin_form_not_valid_one_pass(self):
        form = CaseworkerAdmin(data={
            'username': 'Mahn',
            'first_name': 'Tes',
            'last_name': 'Test123',
            'password1': 'madrese122',
            'email': 'mahnaazi@yahoo.com'

        })
        # print("print form : ", form)
        self.assertFalse(form.is_valid())

    def test_CaseworkerAdmin_form_not_valid_without_mail(self):
        form = CaseworkerAdmin(data={
            'username': 'Mahn',
            'first_name': 'Tes',
            'last_name': 'Test123',
            'password1': 'madrese122',
            'password2': 'madrese122'

        })
        # print("print form : ", form)
        self.assertFalse(form.is_valid())

    def test_CaseworkerAdmin_form_not_valid_without_username(self):
        form = CaseworkerAdmin(data={
            'first_name': 'Tes',
            'last_name': 'Test123',
            'password1': 'madrese122',
            'password2': 'madrese122',
            'email': 'mahnaazi@yahoo.com'

        })
        # print("print form : ", form)
        self.assertFalse(form.is_valid())

    def test_CaseworkerAdmin_no_data(self):
        form = CaseworkerAdmin(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_CaseworkerAdmin_no_data(self):
        form = CaseworkerAdmin(data={'email': 'mahnaazi@yahoo.com'})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
