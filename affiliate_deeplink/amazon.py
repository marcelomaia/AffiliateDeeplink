from urllib import parse

from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.config import AMZ_STORE_NAME
from affiliate_deeplink.utils import add_url_params


class Amazon(BaseDeeplinkGenerator):
    ignore_args = ['tag', 'ref', 'linkId']

    @classmethod
    def get_tracking_url(cls, url):
        parsed_uri = parse.urlparse(url)
        params_dict = dict(parse.parse_qsl(parsed_uri.query))
        params = {'tag': AMZ_STORE_NAME,
                  '_encoding': 'UTF8'}
        for key in params_dict:
            if key not in cls.ignore_args:
                params[key] = params_dict[key]
        url = '{scheme}://{netloc}{path}'.format(scheme=parsed_uri.scheme,
                                                 netloc=parsed_uri.netloc,
                                                 path=parsed_uri.path)
        url = add_url_params(url, params)
        return url
