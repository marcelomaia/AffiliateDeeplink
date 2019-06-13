from ..utils import clear_url, add_url_params


def test_clear_url(dirty_urls):
    original, expected = dirty_urls
    cleared = clear_url(original)
    assert cleared == expected


def test_add_url_param(param_url):
    url, params, expected = param_url
    assert add_url_params(url, params) == expected
