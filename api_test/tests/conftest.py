import pytest

@pytest.fixture(scope="function")
def f_default_header():
    """
    API 기본 Header
    """
    return {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer test-api-token12345"
    }
