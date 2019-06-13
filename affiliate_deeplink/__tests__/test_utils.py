from ..utils import clear_url


def test_clear_url(dirty_urls):
    original, expected = dirty_urls
    cleared = clear_url(original)
    assert cleared == expected
