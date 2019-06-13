from urllib import parse

from .base import BaseDeeplinkGenerator
from .config import MGZ_STORE_NAME


class Magalu(BaseDeeplinkGenerator):
    """
    https://www.magazinevoce.com.br/MGZ_STORE_NAME/[...]
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        parsed_uri = parse.urlparse(url)
        splitted_url = parsed_uri.path.split('/')
        splitted_url[1] = MGZ_STORE_NAME
        new_path = '/'.join(p for p in splitted_url)
        url = '{scheme}://{netloc}{path}'.format(scheme=parsed_uri.scheme,
                                                 netloc=parsed_uri.netloc,
                                                 path=new_path)
        return url
