import logging

from .base import BaseDeeplinkGenerator
from .config import FASTSHOP_AFL_ID, FASTSHOP_AFL_SELLER_NAME
from .utils import add_url_params

log = logging.getLogger(__file__)


class FastShop(BaseDeeplinkGenerator):

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {'sellerId': FASTSHOP_AFL_ID,
                  'sellerName': FASTSHOP_AFL_SELLER_NAME}
        new_url = add_url_params(url, params)
        log.debug(f'old url: {url}. new url {new_url}')
        return new_url
