from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django import urls


class TestCaseworkerRegister(TestCase):

    def create_app_user(self):
        user = User.objects.create_user(
            username="username",
            password="password",
            first_name="first_name",
            email='username@yahoo.com',
        )
        return user

    def setUp(self):
        self.client = Client()

    def test_register_Post_correct(self):

        self.detail_url = reverse('caseworker:register')
        response = self.client.post(self.detail_url, {
            'username': 'username',
            'password1': 'tests123',
            'password2': 'tests123',
            'email': 'username@yahoo.com'
        })
        self.assertEqual(response.status_code, 302)  # fordi vi ikke har looget ind
        # self.assertTemplateUsed(response, 'caseworker/register.html')

    def test_Caseworker_ListView(self):
        self.caseworker_List_url = reverse('caseworker:caseworker')
        response = self.client.get('/caseworker/caseworker')
        self.assertEqual(response.url, self.caseworker_List_url)

    def test_Caseworker_DetailView(self):
        user = self.create_app_user()
        self.caseworker_detail_url = reverse('caseworker:caseworker-detail', args=[user.id])
        response = self.client.get(self.caseworker_detail_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=" + urls.reverse('caseworker:caseworker-detail',
                                                                               args=[user.id]))
        # forid vi ikke er logget ind
