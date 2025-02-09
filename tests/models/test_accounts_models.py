import pytest
from django.contrib.auth import get_user_model


User = get_user_model()
pytestmark = pytest.mark.django_db


class TestCustomUser:
    def test_create_user(self, test_user):
        assert test_user.username is None
        assert test_user.email == "testuser@example.com"
        assert test_user.is_active == True
        assert test_user.is_staff == False
        assert test_user.is_superuser == False

    def test_create_superuser(self, admin_user):
        assert admin_user.username is None
        assert len(admin_user.email) > 0
        assert admin_user.is_active == True
        assert admin_user.is_staff == True
        assert admin_user.is_superuser == True


    @pytest.mark.parametrize(
        "data, error",
        [
            ({}, TypeError),
            ({"email": ""}, TypeError),
            ({"email": "", "password": "foo"}, ValueError),
        ],
    )
    def test_errors_raised(self, data, error):
        with pytest.raises(error):
            User.objects.create_user(**data)

    @pytest.mark.parametrize("data", [
        {"email": "clarke@dailyplanet.com", "password": "testpass123", "is_superuser": False},
                {"email": "clarke@dailyplanet.com", "password": "testpass123", "is_staff": False}

    ])
    def test_superuser_errors_raised(self, data):
        with pytest.raises(ValueError):
            User.objects.create_superuser(**data)
    

    def test___str__(self, test_user):
        assert str(test_user) == test_user.email