import logging

from .base import BaseDeeplinkGenerator
from .config import HURB_CMP_ID
from .utils import clear_url

log = logging.getLogger(__file__)


class Hurb(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        params = {"utm_campaign": HURB_CMP_ID, "cmp": HURB_CMP_ID}
        new_url = clear_url(url, params)
        log.debug(f"old url: {url}. new url {new_url}")
        return new_url
