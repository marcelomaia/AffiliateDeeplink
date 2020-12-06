import logging

from affiliate_deeplink.utils import clear_url

from .base import BaseDeeplinkGenerator
from .config import AMZ_STORE_NAME

log = logging.getLogger(__file__)


class Amazon(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {"tag": AMZ_STORE_NAME, "_encoding": "UTF8"}
        new_url = clear_url(url, params)
        log.debug(f"old url: {url}. new url {new_url}")
        return new_url
