import pytest
from django.contrib.auth import get_user_model


@pytest.fixture
def user_data1():
    return {'username': 'username', 'password1': 'tests123', 'password2': 'tests123', 'email': 'username@yahoo.com'}


@pytest.fixture
def user_data2():
    return {'username': 'user_name', 'password': 'tests123'}


@pytest.fixture
def test_user(user_data2):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data2)
    test_user.set_password(user_data2.get('password'))
    return test_user


@pytest.fixture
def authenticated_user(client, user_data2):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data2)
    test_user.set_password(user_data2.get('password'))
    test_user.save()
    client.login(**user_data2)
    return test_user
