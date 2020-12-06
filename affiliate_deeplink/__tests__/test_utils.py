from ..utils import add_url_params, clear_url


def test_clear_url(dirty_urls):
    original, expected = dirty_urls
    cleared = clear_url(original)
    assert cleared == expected


def test_add_url_param(param_url):
    url, params, expected = param_url
    assert add_url_params(url, params) == expected
