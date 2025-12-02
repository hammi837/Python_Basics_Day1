import pytest

@pytest.fixture
def setup():
    print("Setup: Preparing the test environment")
    yield
    print("Teardown: Cleaning up after the test")

@pytest.fixture
def dataLoad():
    print("Loading test data")
    data = ["Hammad", "Hafeez", "University of Central Punjab"]
    return data

@pytest.fixture(params=["chrome", "firefox", "safari"])
def crossbrowser(request):
    return request.param
