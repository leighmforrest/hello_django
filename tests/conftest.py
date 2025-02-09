import pytest

@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def message():
    return "HAI"