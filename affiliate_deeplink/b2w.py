from .base import BaseDeeplinkGenerator
from .config import BW2_AFL_ID
from .utils import add_url_params


class B2w(BaseDeeplinkGenerator):
    """
        https://www.americanas.com.br/?opn=AFLACOM&epar=b2wafiliados&franq=AFL_ID
        http://www.soubarato.com.br/?opn=B2WAFILIADOS&franq=AFL_ID&epar=b2wafiliados
        https://www.submarino.com.br/?opn=AFLNOVOSUB&franq=AFL_ID&epar=b2wafiliados
        https://www.shoptime.com.br/?opn=AFLSHOP&franq=AFL_ID&epar=b2wafiliados
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {'franq': BW2_AFL_ID,
                  'epar': 'b2wafiliados',
                  'hl': 'lower'}
        if 'americanas.com.br' in url:
            params['opn'] = 'AFLACOM'
        elif 'submarino.com.br' in url:
            params['opn'] = 'AFLNOVOSUB'
        elif 'shoptime.com.br' in url:
            params['opn'] = 'AFLSHOP'
        url = add_url_params(url, params)
        return url
