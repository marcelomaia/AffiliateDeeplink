from .afilio import Afilio
from .amazon import Amazon
from .b2w import B2w
from .banggood import Banggood
from .hurb import Hurb
from .lomadee import Lomadee
from .magazine_luiza import Magalu
from .natura import Natura
from .zanox import Zanox


def _is_b2w(url):
    urls_b2w = ['americanas.com.br', 'submarino.com.br', 'shoptime.com.br', 'soubarato.com.br']
    for tst in urls_b2w:
        if tst in url:
            return True
    return False


def _is_magazine(url):
    return 'magazinevoce.com.br' in url


def _is_amazon(url):
    return 'amazon.com' in url


def _is_natura(url):
    return 'natura.com.br' in url


def _is_banggood(url):
    return 'banggood.com' in url


def _is_netshoes(url):
    return 'netshoes.com' in url


def _is_hotel_urbano(url):
    return 'hurb.com' in url or 'hotelurbano.com' in url


def generate_deeplink(url: str) -> str:
    # TODO, let user select deeplink generator order
    if _is_b2w(url):
        return B2w.get_tracking_url(url)
    elif _is_magazine(url):
        return Magalu.get_tracking_url(url)
    elif _is_amazon(url):
        return Amazon.get_tracking_url(url)
    elif _is_natura(url):
        return Natura.get_tracking_url(url)
    elif _is_banggood(url):
        return Banggood.get_tracking_url(url)
    elif _is_netshoes(url):
        return Lomadee.get_tracking_url(url)
    elif _is_hotel_urbano(url):
        return Hurb.get_tracking_url(url)
    else:
        deeplink = Zanox.get_tracking_url(url)
        if not deeplink:
            deeplink = Afilio.get_tracking_url(url)
            if not deeplink:
                deeplink = Lomadee.get_tracking_url(url)
        return deeplink
