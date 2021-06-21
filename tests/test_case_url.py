from django import urls
import pytest
from django.contrib.auth import get_user_model
from case.models import CaseInfo

url_data = [
    ('case:caseinfo-view', 302),
    ('case:report-login', 200),
    ('case:revisit-login', 200),
]


@pytest.mark.parametrize("url, expected", url_data)
def test_case_views(client, url, expected):
    temp_url = urls.reverse(url)
    resp = client.get(temp_url)
    assert resp.status_code == expected


@pytest.mark.django_db
def test_user_login(client, user_data_for_login, create_user_for_login):
    user_model = get_user_model()
    assert user_model.objects.count() == 1  # Når vi kalder create_user_model in i modelen opreetter vi en user
    login_url = urls.reverse('caseworker:login')
    resp = client.post(login_url, data=user_data_for_login)  # Her poster en login-data til login-side
    assert resp.status_code == 302
    assert resp.url == urls.reverse('case:caseinfo-view')  # Når man logger ind så bliver man redirected til "/case/"


@pytest.mark.django_db
def test_Login_CaseInfo_Cases_ListView(client, user_data_for_login, create_user_for_login, case_info_data):
    test_user_login(client, user_data_for_login, create_user_for_login)
    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:caseinfo-cases-view', kwargs={'id': case_info.id})  # Se sagerne under en sagsinfo
    resp = client.get(user_url)
    assert resp.status_code == 200   # Fordi vi er logget ind bliver vi ikke redirectet
    assert "Go back" in str(resp.content)
