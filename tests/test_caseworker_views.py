from django import urls
from django.contrib.auth import get_user_model
import pytest
from django.contrib.auth.models import User

# Data til data-drevet test
url_data = [
    ('caseworker:register', 302),
    ('caseworker:logout', 302),
    ('caseworker:login', 200),
    ('caseworker:caseworker', 302),
]


@pytest.mark.parametrize("url, expected", url_data)  # url er adressen og expected er response-kode i url_data
def test_logged_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)  # Client er som en browser som vil bruge urlen
    assert resp.status_code == expected  # Når man ikke er logget ind så vil de redirect til login-side


@pytest.mark.django_db
def test_user_login_home_view(client, user_data_for_login, create_user_for_login):
    user_model = get_user_model()
    assert user_model.objects.count() == 1  # Når vi kalder create_user_model in i modelen opreetter vi en user
    login_url = urls.reverse('caseworker:login')
    resp = client.post(login_url, data=user_data_for_login)  # Her poster en login-data til login-side
    assert resp.status_code == 302
    assert resp.url == urls.reverse('case:caseinfo-view')  # Når man logger ind så bliver man redirected til "/case/"
    user_url = urls.reverse('caseworker:caseworker')  # Se sagsbehandlere liste
    resp = client.get(user_url)
    assert resp.status_code == 200  # Fordi vi er logget ind bliver vi ikke redirectet


@pytest.mark.django_db
def test_user_register(client, user_data_for_login, create_user_for_login, user_data_for_register):
    user_model = get_user_model()
    assert user_model.objects.count() == 1  # Når vi kalder create_user_model in i modelen opreetter vi en user
    login_url = urls.reverse('caseworker:login')
    resp = client.post(login_url, data=user_data_for_login)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('case:caseinfo-view')  # Når man logger ind så bliver man redirected til "/case/"
    register_url = urls.reverse('caseworker:register')  # Vi vil registere en ny bruger efter vi har logget ind
    response = client.post(register_url, user_data_for_register)
    assert user_model.objects.count() == 2  # Ny bruger bliver rigistered så skal være 2 bruger ind i database
    assert response.status_code == 302
    assert response.url == urls.reverse('case:caseinfo-view')


url_data_2 = [
    ('caseworker:login', 200),
    ('caseworker:logout', 200),
    ('caseworker:caseworker', 200),

]


@pytest.mark.django_db
@pytest.mark.parametrize("url, expected", url_data_2)  # Test at man kan se siderene når man er logget ind
def test_logged_in_user_can_access_pages(client, user_data_for_login, create_user_for_login, url, expected):
    login_url = urls.reverse('caseworker:login')
    resp = client.post(login_url, data=user_data_for_login)
    assert resp.status_code == 302
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)  # Client er som en browser som vil bruge urlen
    assert resp.status_code == expected


@pytest.mark.django_db
def test_logged_in_user_can_access_caseworker_detail(client, create_user_for_login, user_data_for_login):
    login_url = urls.reverse('caseworker:login')
    resp = client.post(login_url, data=user_data_for_login)
    assert resp.status_code == 302
    detail_url = urls.reverse('caseworker:caseworker-detail', kwargs={'pk': create_user_for_login.id})
    resp = client.get(detail_url)
    assert resp.status_code == 200
    assert "Sagsbehandler" in str(resp.content)  # tjekker også sidens indhold
    assert "user_name" in str(resp.content)  # tjekker username er i sidens indhold


@pytest.mark.django_db
def test_user_logout(client):
    logout_url = urls.reverse('caseworker:logout')
    resp = client.get(logout_url)
    assert resp.status_code == 302  # Vi får 302 og redirect til login side fordi vi ikke har logget ind
    assert resp.url == "/accounts/login/?next=/caseworker/logout/"


@pytest.mark.django_db
def test_user_create_db_data():  # Test at man kan oprette en bruger i databasen (integration test)
    User.objects.create_user('user_name')
    assert User.objects.all().count() == 1
