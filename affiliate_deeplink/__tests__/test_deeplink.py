import pytest

from ..afilio import Afilio
from ..amazon import Amazon
from ..awin import Awin
from ..b2w import B2w
from ..banggood import Banggood
from ..base import BaseDeeplinkGenerator
from ..hurb import Hurb
from ..lomadee import Lomadee
from ..magazine_luiza import Magalu
from ..natura import Natura
from .. import Shopee
from ..zanox import Zanox
from .constants import (
    AFILIO_SUCESS,
    LOMADEE_INVALID_SOURCE_ID,
    LOMADEE_INVALID_URL_REQ,
    LOMADEE_SUCESS_REQ,
    SHOPEE_SHORTLINK_SUCCESS,
    ZANOX_ERROR,
    ZANOX_SUCESS,
)


def helper(urls, _class):
    original, expected = urls
    deeplink = _class.get_tracking_url(original)
    assert deeplink == expected


def test_banggood(bangood_url):
    helper(bangood_url, Banggood)


def test_hurb(hurb_url):
    helper(hurb_url, Hurb)


def test_b2w(b2w_url):
    helper(b2w_url, B2w)


def test_amazon(amazon_url):
    helper(amazon_url, Amazon)


def test_awin(awin_url):
    helper(awin_url, Awin)


def test_natura(natura_url):
    helper(natura_url, Natura)


def test_magalu(magalu_url):
    helper(magalu_url, Magalu)


def test_magalu_novo_url(magalu_novo_url):
    helper(magalu_novo_url, Magalu)


def test_shopee(monkeypatch, shopee_url):
    original, expected = shopee_url

    class MockResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return SHOPEE_SHORTLINK_SUCCESS

    def mock_post(url, headers=None, data=None, timeout=None):
        assert "open-api.affiliate.shopee.com.br/graphql" in url
        assert headers["Content-Type"] == "application/json"
        assert headers["Authorization"].startswith("SHA256 Credential=")
        assert '"originUrl":"https://shopee.com.br/produto-exemplo-i.123456.7890123456"' in data
        assert "sp_atk" not in data
        return MockResponse()

    monkeypatch.setattr("affiliate_deeplink.shopee.requests.post", mock_post)
    monkeypatch.setattr("affiliate_deeplink.shopee.SHOPEE_APP_ID", "APP_ID")
    monkeypatch.setattr("affiliate_deeplink.shopee.SHOPEE_APP_SECRET", "APP_SECRET")
    monkeypatch.setattr("affiliate_deeplink.shopee.time.time", lambda: 1710000000)

    deeplink = Shopee.get_tracking_url(original)
    assert deeplink == expected


def test_lomadee(monkeypatch, lomadee_url):
    helper(lomadee_url, Lomadee)


def test_afilio(monkeypatch, afilio_url):
    def mockreturn(param):
        _, expected = afilio_url
        return AFILIO_SUCESS

    monkeypatch.setattr(Afilio, "_req_afilio", mockreturn)
    helper(afilio_url, Afilio)


def test_zanox(monkeypatch, zanox_url):
    def mockreturn(param):
        _, expected = zanox_url
        return ZANOX_SUCESS

    monkeypatch.setattr(Zanox, "_req_zanox", mockreturn)
    helper(zanox_url, Zanox)


def test_zanox_invalid(monkeypatch, zanox_invalid_url):
    def mockreturn(param):
        _, expected = zanox_invalid_url
        return ZANOX_ERROR

    monkeypatch.setattr(Zanox, "_req_zanox", mockreturn)
    helper(zanox_invalid_url, Zanox)


def test_base_deeplink():
    with pytest.raises(NotImplementedError):
        BaseDeeplinkGenerator.get_tracking_url("some url")

    with pytest.raises(NotImplementedError):
        BaseDeeplinkGenerator.get_sales_report("start date", "end date")
