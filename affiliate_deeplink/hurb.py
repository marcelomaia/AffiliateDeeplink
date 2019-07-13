from .base import BaseDeeplinkGenerator
from .config import HURB_CMP_ID
from .utils import clear_url


class Hurb(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {'utm_campaign': HURB_CMP_ID,
                  'cmp': HURB_CMP_ID}
        cleared_url = clear_url(url, params)
        return cleared_url
