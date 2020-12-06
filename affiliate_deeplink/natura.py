import logging
from urllib import parse

from affiliate_deeplink.utils import clear_url

from .base import BaseDeeplinkGenerator
from .config import NATURA_CONSULTORIA_NAME

log = logging.getLogger(__file__)


class Natura(BaseDeeplinkGenerator):
    """
    https://www.natura.com.br/[...]?consultoria=NATURA_CONSULTORIA_NAME
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        url_clear = clear_url(url)
        parsed_uri = parse.urlparse(url_clear)
        query = "consultoria={}&a=a".format(NATURA_CONSULTORIA_NAME)
        new_url = "{scheme}://{netloc}{path}?{query}".format(
            scheme=parsed_uri.scheme,
            netloc=parsed_uri.netloc,
            path=parsed_uri.path,
            query=query,
        )
        log.debug(f"old url: {url}. new url {new_url}")
        return new_url
