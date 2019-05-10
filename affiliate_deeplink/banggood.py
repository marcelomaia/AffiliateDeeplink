from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.config import BANGGOOD_REFERENCE_ID
from affiliate_deeplink.utils import clear_url


class Banggood(BaseDeeplinkGenerator):

    @classmethod
    def get_tracking_url(cls, url):
        params = {'p': BANGGOOD_REFERENCE_ID}
        clear_url(url, params)
        return url
