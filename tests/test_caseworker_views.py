from django.test import TestCase, Client
from django.urls import reverse


class TestCaseworkerRegister(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_Post_wrong(self):

        self.detail_url = reverse('caseworker:register')
        response = self.client.post(self.detail_url, {
            'username': 'username',
            'password1': 'tests123',
            'password2': 'tests123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'caseworker/register.html')

    def test_register_Post_correct(self):

        self.detail_url = reverse('caseworker:register')
        print("self.detail_url :::  ", self.detail_url)
        response = self.client.post(self.detail_url, {
            'username': 'username',
            'password1': 'tests123',
            'password2': 'tests123',
            'email': 'username@yahoo.com'
        })
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, '/case')
