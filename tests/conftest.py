import pytest
from django.contrib.auth import get_user_model
from case.models import CaseInfo, Status, Case
from caseworker.models import Company, Country, PostalCode, Address


@pytest.fixture
def user_data_for_register():
    return {
        'username': 'my_username',
        'password1': 'my_password123',
        'password2': 'my_password123',
        'email': 'username@yahoo.com'
    }


@pytest.fixture
def user_data_for_login():
    return {'username': 'user_name', 'password': 'tests123'}


@pytest.fixture
def create_user_for_login(user_data_for_login):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data_for_login)
    return test_user


@pytest.fixture
def case_info_data():
    country_name = Country.objects.create(name='Denmark')
    postal_code = PostalCode.objects.create(post_code='2100', city_name='Copenhagen', country=country_name)
    address = Address.objects.create(street='street1', post_code=postal_code)
    company = Company.objects.create(name='company1', address=address)
    status = Status.objects.create()
    case_info = CaseInfo.objects.create(status=status, company=company)
    return case_info, company, status


@pytest.fixture
def status_data():
    status = Status.objects.create()
    status.status = status.CASESTATUS[2][1]
    return status


@pytest.fixture
def case_data():
    country_name = Country.objects.create(name='Denmark')
    postal_code = PostalCode.objects.create(post_code='2100', city_name='Copenhagen', country=country_name)
    address = Address.objects.create(street='street1', post_code=postal_code)
    company = Company.objects.create(name='company1', address=address)
    status = Status.objects.create()
    case_info = CaseInfo.objects.create(status=status, company=company)
    case = Case.objects.create(title='Title 1', description='Description 1', case_info=case_info)
    return case
