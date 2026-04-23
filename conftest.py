import pytest

def pytest_addoption(parser):
    parser.addoption("--app-url", action="store")

@pytest.fixture
def app_url(request):
    return request.config.getoption("--app-url")