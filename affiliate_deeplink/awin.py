import logging
from urllib import parse
from urllib.parse import urlparse

from .base import BaseDeeplinkGenerator
from .config import AWIN_ACCEPTED_DOMAINS, AWIN_ADS_SPACE_ID
from .utils import clear_url

log = logging.getLogger(__file__)


class AwinException(Exception):
    pass


class Awin(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        """More info here: http://wiki.awin.com/index.php/Deeplink_Builder."""
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc.replace("www.", "")
        if domain not in AWIN_ACCEPTED_DOMAINS.keys():
            log.debug(f"domain {domain} not supported yet")
            return ""
        parsed_url = parse.quote_plus(clear_url(url))
        advertiser_id = AWIN_ACCEPTED_DOMAINS.get(domain)
        new_url = f"https://www.awin1.com/cread.php?awinmid={advertiser_id}&awinaffid={AWIN_ADS_SPACE_ID}&ued={parsed_url}"
        log.debug(f"old url: {url}. new url {new_url}")
        return new_url
