from django import urls
from django.contrib.auth import get_user_model
import pytest
from django.contrib.auth.models import User


url_data = [
    ('caseworker:register', 302),
    ('caseworker:logout', 302),
    ('caseworker:login', 200),
    ('case:case-view', 302),
    ('case:case-create', 302),

]


@pytest.mark.parametrize("u, expected", url_data)
def test_logged_views(client, u, expected, user_data1):
    temp_url = urls.reverse(u)
    resp = client.get(temp_url)
    assert resp.status_code == expected


@pytest.mark.parametrize('param', [
    'caseworker:register',
    'caseworker:logout'
])
def test_render1_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_register(client, user_data1):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    create_user_url = urls.reverse('caseworker:register')
    resp = client.post(create_user_url, user_data1)
    print("client.post:  ", resp)
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_login(client, test_user_login_fixture, user_data2):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('caseworker:login')
    resp = client.post(login_url, data=user_data2)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('case:case-view')


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = urls.reverse('caseworker:logout')
    resp = client.get(logout_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_detail(client, new_user1):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('case:case-detail', kwargs={'pk': new_user1.id})
    resp = client.get(login_url)
    assert resp.status_code == 302
    # assert resp.url == urls.reverse('case:case-detail', kwargs={'pk': new_user1.id})


@pytest.mark.django_db
def test_case_delete(client, test_user_login_fixture):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('case:case-delete', kwargs={'pk': test_user_login_fixture.id})
    resp = client.post(login_url)
    assert resp.status_code == 302
    # assert user_model.objects.filter(pk=new_user1.id).exists() == False


@pytest.mark.django_db
def test_user_create_db_data():
    User.objects.create_user('user_name')
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_user1_create_db(new_user1):
    print("new_user2:  ", new_user1)
    count = User.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_user2_create_db(new_user2):
    print("new_user2:  ", new_user2)
    count = User.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_user_db_not_data():
    count = User.objects.all().count()
    assert count == 0
