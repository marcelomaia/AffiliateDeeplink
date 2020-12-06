import logging

from .base import BaseDeeplinkGenerator
from .config import BANGGOOD_REFERENCE_ID
from .utils import clear_url

log = logging.getLogger(__file__)


class Banggood(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {"p": BANGGOOD_REFERENCE_ID}
        new_url = clear_url(url, params)
        log.debug(f"old url: {url}. new url {new_url}")
        return new_url
