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
        return {"totallooseoffers": 0, "details": {
            "date": {"valid": True, "eonandyear": {"lowestsetbit": 0}, "hour": 17, "month": 6, "year": 2019,
                     "timezone": -180, "millisecond": 174, "xmlschematype": {"prefix": "", "localpart": "dateTime",
                                                                             "namespaceuri": "http://www.w3.org/2001/XMLSchema"},
                     "day": 13, "minute": 51, "second": 1}, "code": 0, "applicationversion": "v1",
            "applicationid": "3651516a44624e526551453d", "elapsedtime": 42, "message": "success", "status": "success"},
                "lomadeelinks": [{"lomadeelink": {"originallink": "http://americanas.com.br", "code": 0, "id": 1,
                                                  "redirectlink": "https://iuuuupiiii.com"}}],
                "page": 1, "totalpages": 1, "totalresultsreturned": 1, "totalresultsavailable": 1}

    monkeypatch.setattr(Lomadee, "_req_lomadee", mockreturn)
    helper(lomadee_url, Lomadee)
