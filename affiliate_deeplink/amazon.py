import os

from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.utils import add_url_params


class Amazon(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url):
        params = {'tag': os.getenv('AMZ_STORE_NAME'),
                  '_encoding': 'UTF8'}
        url = add_url_params(url, params)
        return url
