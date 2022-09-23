import pytest

pytest_plugins = ("celery.contrib.pytest",)


@pytest.fixture(scope="session")
def celery_config():
    print('hi i am celery_config')
    return {
        "broker_url": "memory://",
        "result_backend": "cache+memory://",
        "cache_backend": "memory",
    }


