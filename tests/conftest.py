import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid
from django_dynamic_fixture import G


@pytest.fixture
def authenticated_user_new(client):
    """Create an authenticated user for a test"""
    user = G(User, username='my_username')
    user.set_password('my_password123')
    user.save()
    client.login(username='my_username', password='my_password123')
    return user


@pytest.fixture
def user_data1():
    return {'username': 'username', 'password1': 'tests123', 'password2': 'tests123', 'email': 'username@yahoo.com'}


@pytest.fixture
def user_data2():
    return {'username': 'user_name', 'password': 'tests123'}


@pytest.fixture
def case_data1():
    return {
        'title': 'Unit test case title 1',
        'description': 'Unit test case description 1',
        'case_info': uuid.uuid4()
            }


@pytest.fixture
def test_user_login_fixture(user_data2):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data2)
    test_user.set_password(user_data2.get('password5'))
    return test_user


@pytest.fixture
def authenticated_user(client, user_data2):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data2)
    test_user.set_password(user_data2.get('password'))
    test_user.save()
    client.login(**user_data2)
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
    return new_user_factory("Test_user", "password", "MyName")


@pytest.fixture
def new_user2(db, new_user_factory):
    return new_user_factory("Test_user", "password", "MyName", is_staff="True")
