from django.test import TestCase
from caseworker.forms import CaseworkerAdmin
# from caseworker.models import Company, Country, PostalCode, Address


class TestForms(TestCase):

    def test_CaseworkerAdmin_form_true(self):
        form = CaseworkerAdmin(data={
            'username': 'username',
            'password1': 'tests123',
            'password2': 'tests123',
            'email': 'username@yahoo.com'

        })
        # print("print form : ", form)
        self.assertTrue(form.is_valid())

    def test_CaseworkerAdmin_form_not_valid_one_pass(self):
        form = CaseworkerAdmin(data={
            'username': 'username',
            'password1': 'tests123',
            'email': 'username@yahoo.com'

        })
        # print("print form : ", form)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Der er en enkelt fejl

    def test_CaseworkerAdmin_form_not_valid_without_mail(self):
        form = CaseworkerAdmin(data={
            'username': 'Mahn',
            'password1': 'madrese122',
            'password2': 'madrese122'

        })
        # print("print form : ", form)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_CaseworkerAdmin_form_not_valid_with_wrong_password(self):
        form = CaseworkerAdmin(data={
            'username': 'Mahnaz',
            'password1': 'Mahnaz1234',
            'password2': 'Mahnaz1234',
            'email': 'mahnaazi@yahoo.com'

        })
        # print("print form : ", form)
        self.assertFalse(form.is_valid())

    def test_CaseworkerAdmin_form_not_valid_without_username(self):
        form = CaseworkerAdmin(data={
            'password1': 'madrese122',
            'password2': 'madrese122',
            'email': 'mahnaazi@yahoo.com'

        })
        # print("print form : ", form)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_CaseworkerAdmin_no_data(self):
        form = CaseworkerAdmin(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_CaseworkerAdmin_no_3_data(self):
        form = CaseworkerAdmin(data={'email': 'mahnaazi@yahoo.com'})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
