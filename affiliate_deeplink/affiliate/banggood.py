from urllib import parse

from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.config import BANGGOOD_REFERENCE_ID
from affiliate_deeplink.utils import add_url_params


class Banggood(BaseDeeplinkGenerator):
    ignore_args = ['p', 'utm_campaign', 'utm_content', 'custlinkid']

    @classmethod
    def get_tracking_url(cls, url):
        parsed_uri = parse.urlparse(url)
        params_dict = dict(parse.parse_qsl(parsed_uri.query))
        params = {'p': BANGGOOD_REFERENCE_ID}
        for key in params_dict:
            if key not in cls.ignore_args:
                params[key] = params_dict[key]
        url = '{scheme}://{netloc}{path}'.format(scheme=parsed_uri.scheme,
                                                 netloc=parsed_uri.netloc,
                                                 path=parsed_uri.path)
        url = add_url_params(url, params)
        return url
