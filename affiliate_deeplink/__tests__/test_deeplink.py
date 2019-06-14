from .constants import LOMADEE_SUCESS_REQ, LOMADEE_INVALID_URL_REQ, LOMADEE_INVALID_SOURCE_ID, AFILIO_SUCESS
from ..afilio import Afilio
from ..amazon import Amazon
from ..b2w import B2w
from ..banggood import Banggood
from ..lomadee import Lomadee
from ..magazine_luiza import Magalu
from ..natura import Natura


def helper(urls, _class):
    original, expected = urls
    deeplink = _class.get_tracking_url(original)
    assert deeplink == expected


def test_banggood(bangood_url):
    helper(bangood_url, Banggood)


def test_b2w(b2w_url):
    helper(b2w_url, B2w)


def test_amazon(amazon_url):
    helper(amazon_url, Amazon)


def test_natura(natura_url):
    helper(natura_url, Natura)


def test_magalu(magalu_url):
    helper(magalu_url, Magalu)


def test_lomadee(monkeypatch, lomadee_url):
    def mockreturn(param):
        _, expected = lomadee_url
        return LOMADEE_SUCESS_REQ

    monkeypatch.setattr(Lomadee, "_req_lomadee", mockreturn)
    helper(lomadee_url, Lomadee)


def test_lomadee_fail(monkeypatch, lomadee_url_invalid):
    def mockreturn(param):
        _, expected = lomadee_url_invalid
        return LOMADEE_INVALID_URL_REQ

    monkeypatch.setattr(Lomadee, "_req_lomadee", mockreturn)
    helper(lomadee_url_invalid, Lomadee)


def test_lomadee_invalid_source_id(monkeypatch, lomadee_url_invalid):
    def mockreturn(param):
        _, expected = lomadee_url_invalid
        return LOMADEE_INVALID_SOURCE_ID

    monkeypatch.setattr(Lomadee, "_req_lomadee", mockreturn)
    helper(lomadee_url_invalid, Lomadee)


def test_afilio(monkeypatch, afilio_url):
    def mockreturn(param):
        _, expected = afilio_url
        return AFILIO_SUCESS

    monkeypatch.setattr(Afilio, "_req_afilio", mockreturn)
    helper(afilio_url, Afilio)
