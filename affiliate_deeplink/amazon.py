from affiliate_deeplink.utils import clear_url
from .base import BaseDeeplinkGenerator
from .config import AMZ_STORE_NAME


class Amazon(BaseDeeplinkGenerator):

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {'tag': AMZ_STORE_NAME,
                  '_encoding': 'UTF8'}
        url = clear_url(url, params)
        return url
