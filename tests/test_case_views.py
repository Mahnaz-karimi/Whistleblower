from django import urls
import pytest
from django.contrib.auth import get_user_model
from case.models import CaseInfo, Case


# Data til data-drevet test
url_data = [
    ('case:caseinfo-view', 302),
    ('case:report-login', 200),
    ('case:revisit-login', 200),
]


@pytest.mark.parametrize("url, expected", url_data)  # Data-drevet test
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
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind

    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:caseinfo-cases-view', kwargs={'id': case_info.id})  # Se sagerne under en sagsinfo
    resp = client.get(user_url)
    assert resp.status_code == 200   # Fordi vi er logget ind bliver vi ikke redirectet
    assert "Go back" in str(resp.content)


@pytest.mark.django_db
def test_Login_CaseInfo_Delete(client, user_data_for_login, create_user_for_login, case_info_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind

    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:caseinfo-delete', kwargs={'pk': case_info.id})  # Se sagerne under en sagsinfo
    resp = client.post(user_url)
    assert resp.status_code == 302   # bliver
    assert resp.url == urls.reverse('case:caseinfo-view')  # Tjekkes at at de home view som viser alle caseinfo


@pytest.mark.django_db
def test_Login_CaseInfo_Update(client, user_data_for_login, create_user_for_login, case_info_data, status_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind

    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:caseinfo-update', kwargs={'pk': case_info.id})  # Vælges case-info for at update
    resp = client.post(user_url, {
            'caseworker': create_user_for_login.id,
            'status': status_data.id,
        })
    assert resp.status_code == 302  # Efter at update caseinfoen,  bliver redirectet til home view
    assert resp.url == urls.reverse('case:caseinfo-view')  # Home view


@pytest.mark.django_db
def test_Case_New_CreateView_Post(client, user_data_for_login, create_user_for_login, case_info_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind

    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:case-create-new', kwargs={'id': case_info.id})  # Vælges case-info for at update
    resp = client.post(user_url, {
            'title': 'Unit test case title 1',
            'description': 'Unit test case description 1',
        })
    assert resp.status_code == 302  # Efter at update caseinfoen,  bliver redirectet til home view
    assert resp.url == urls.reverse('case:caseinfo-view')  # Home view


@pytest.mark.django_db
def test_Case_DetailView_Get(client, user_data_for_login, create_user_for_login, case_data):
    test_user_login(client, user_data_for_login, create_user_for_login)  # Her logger vi ind

    case = Case.objects.latest('pk')
    user_url = urls.reverse('case:case-detail', kwargs={'pk': case.pk})  # Vælges case-info for at update
    resp = client.get(user_url)
    assert resp.status_code == 200  # Efter at update caseinfoen,  bliver redirectet til home view
    assert "Title 1" in str(resp.content)


@pytest.mark.django_db
def test_ReportCreateView_Post(client,  case_info_data):
    session = client.session
    session['cmp_guid'] = 'valid'
    session.save()

    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:new-report', kwargs={'id': case_info.id})  # oprettes en caseinfo for at kanne report
    resp = client.get(user_url)
    assert resp.status_code == 200  #
    assert "Anmeldelse" in str(resp.content)


@pytest.mark.django_db
def test_RevisitCaseInfoView(client, case_info_data):
    session = client.session
    session['case_guid'] = 'valid'
    session.save()

    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:revisit-report', kwargs={'id': case_info.id})  # Vælges case-info for at update
    resp = client.get(user_url)
    assert resp.status_code == 200  # Den bliver ikke redirecti til login gense og case info fundet.
    assert "Information om din anmedelse" in str(resp.content)


@pytest.mark.django_db
def test_RevisitCaseNewCreateView(client, case_info_data):
    session = client.session
    session['info_guid'] = 'valid'
    session.save()

    case_info = CaseInfo.objects.latest('pk')
    user_url = urls.reverse('case:revisit-case-new', kwargs={'id': case_info.id})  # Vælges case-info for at update
    resp = client.get(user_url)
    assert resp.status_code == 200  # Den bliver ikke redirecti til login gense og case info fundet.
    assert "Anmeldelse" in str(resp.content)
