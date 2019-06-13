from .base import BaseDeeplinkGenerator
from .config import BANGGOOD_REFERENCE_ID
from .utils import clear_url


class Banggood(BaseDeeplinkGenerator):

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {'p': BANGGOOD_REFERENCE_ID}
        cleared_url = clear_url(url, params)
        return cleared_url
