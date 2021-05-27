from django import urls
from django.contrib.auth import get_user_model
import pytest
from django.contrib.auth.models import User


@pytest.mark.parametrize('param', [
    'case_worker:register',
    'case_worker:login',
    'case_worker:logout'
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_register(client, user_data1):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    create_user_url = urls.reverse('case_worker:register')
    resp = client.post(create_user_url, user_data1)
    assert user_model.objects.count() == 1
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_login(client, test_user, user_data2):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('case_worker:login')
    resp = client.post(login_url, data=user_data2)
    assert resp.status_code == 302
    # assert resp.url == urls.reverse('case/')


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = urls.reverse('case_worker:logout')
    resp = client.get(logout_url)
    assert resp.status_code == 200
    # assert resp.url == urls.reverse('/caseworker/logout/')


@pytest.mark.django_db
def test_user_create_db():
    User.objects.create_user('test', 'test@test.com', 'test')
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_user_create1_db():
    count = User.objects.all().count()
    assert count == 0
