from django import urls
from django.contrib.auth import get_user_model
import pytest
from django.contrib.auth.models import User

url_data = [
    ('caseworker:register', 302),
    ('caseworker:logout', 302),
    ('caseworker:login', 200),
    ('caseworker:caseworker', 302),
]


@pytest.mark.parametrize("url, expected", url_data)  # url er stringen og expected er de tal i url_data
def test_logged_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)  # client er som en bruger som vil bruge de url in i "url_data"
    assert resp.status_code == expected


@pytest.mark.parametrize('param', [  # den er det samme ovenover exp men her bruger vi kun en parameter
    'caseworker:register',
    'caseworker:logout'
])
def test_render1_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_register(client, user_data_for_register):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    create_user_url = urls.reverse('caseworker:register')
    resp = client.post(create_user_url, user_data_for_register)
    assert resp.status_code == 302  # User ikke logget ind: redirect
    assert resp.url == "/accounts/login/?next=/caseworker/register/"  # til log ind side


@pytest.mark.django_db
def test_user_login(client, user_data_for_login, create_user_model):
    user_model = get_user_model()
    assert user_model.objects.count() == 1  # Når vi kalder create_user_model in i modelen opreetter vi en user
    login_url = urls.reverse('caseworker:login')
    resp = client.post(login_url, data=user_data_for_login)
    assert resp.status_code == 302
    assert resp.url == "/case/"  # når man logger ind så bliver redirected
    assert resp.url == urls.reverse('case:caseinfo-view')
    register_url = urls.reverse('caseworker:register')  # vi vil registere en ny bruger efter vi har logget ind
    response = client.post(register_url, {
        'username': 'my_username',
        'password1': 'my_password123',
        'password2': 'my_password123',
        'email': 'username@yahoo.com'
    })
    assert user_model.objects.count() == 2  # ny bruger bliver rigistered så skal være 2 bruger ind i database
    assert response.status_code == 302
    assert response.url == "/case"

    user_url = urls.reverse('caseworker:caseworker')  # Se sagsbehandlere liste
    resp = client.get(user_url)
    assert resp.status_code == 200  # fordi vi er logget ind

    detail_url = urls.reverse('caseworker:caseworker-detail', kwargs={'pk': create_user_model.id})
    resp = client.get(detail_url)
    assert resp.status_code == 200  # fordi vi er logget ind

    logout_url = urls.reverse('caseworker:logout')  # her logger vi ud
    resp = client.get(logout_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_logout(client):
    logout_url = urls.reverse('caseworker:logout')
    resp = client.get(logout_url)
    assert resp.status_code == 302  # Vi får 302 og redirect til login side fordi vi ikke har logget ind
    assert resp.url == "/accounts/login/?next=/caseworker/logout/"


@pytest.mark.django_db
def test_user_view(client):
    user_url = urls.reverse('caseworker:caseworker')
    resp = client.get(user_url)
    assert resp.status_code == 302  # fordi vi ikke er logget ind så redirect to log ind side


@pytest.mark.django_db
def test_user_detail(client, create_user_model):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    detail_url = urls.reverse('caseworker:caseworker-detail', kwargs={'pk': create_user_model.id})
    resp = client.get(detail_url)
    assert resp.status_code == 302  # fordi vi ikke er logget ind så redirect to log ind side
    assert resp.url == "/accounts/login/?next=" + urls.reverse('caseworker:caseworker-detail',
                                                               kwargs={'pk': create_user_model.id})


@pytest.mark.django_db
def test_user_create_db_data():  # Her opretter en user med det samme
    User.objects.create_user('user_name')
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_user1_create_db(new_user1):  # Her kalder vi en metode som opretter en user ind i fixture
    count = User.objects.all().count()
    assert count == 1


@pytest.mark.django_db
def test_user_db_not_data():
    count = User.objects.all().count()  # Her tjekker vi at database er tom
    assert count == 0
