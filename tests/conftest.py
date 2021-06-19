import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


@pytest.fixture
def user_data_for_register():
    return {'username': 'username', 'password1': 'tests123', 'password2': 'tests123', 'email': 'username@yahoo.com'}


@pytest.fixture
def user_data_for_login():
    return {'username': 'user_name', 'password': 'tests123'}


@pytest.fixture
def create_user_model(client, user_data_for_login):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data_for_login)
    return test_user


@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
        return user
    return create_app_user


@pytest.fixture
def new_user1(db, new_user_factory):
    return new_user_factory("Test_user")


'''
from django_dynamic_fixture import G


@pytest.fixture
def authenticated_user_and_save(client):
    """Create an authenticated user for a test"""
    user = G(User, username='my_username')
    user.set_password('my_password123')
    user.save()
    client.login(username='my_username', password='my_password123')
    return user
'''
