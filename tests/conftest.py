import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def test_user():
    yield get_user_model().objects.create_user(email="testuser@example.com", password="test_password")
