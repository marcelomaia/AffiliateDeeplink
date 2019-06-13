import pytest


@pytest.fixture
def meal_kit():
    return 2


@pytest.fixture(scope="function", params=['4h', '6h', '8h'])
def order_meal_kit(request):
    return 1
