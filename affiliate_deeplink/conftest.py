import os

import pytest

from .utils import clear_url

BASEDIR = os.path.dirname(os.path.abspath(__file__))
links = []

with open(os.path.join(BASEDIR, '__tests__', 'links.txt'), 'r') as f:
    lines = f.readlines()
    for line in lines:
        original, expected = line.split(';')
        links.append((original.strip(), expected.strip()))


@pytest.fixture(scope='function', params=links)
def dirty_urls(request):
    return request.param


@pytest.fixture
def make_clean_url():
    def _make_clean_url(url):
        return clear_url(url)

    return _make_clean_url


@pytest.fixture(scope="function", params=['4h', '6h', '8h'])
def order_meal_kit(request):
    return 1
