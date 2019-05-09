import logging
from urllib import parse

import requests

from affiliate_deeplink.config import ignore_args
from affiliate_deeplink.utils import clear_url
from .base import BaseDeeplinkGenerator
from .config import ZANOX_ADS_SPACE_ID, ZANOX_CONNECT_ID
from .utils import add_url_params

logger = logging.getLogger('deeplink.zanox')


class Zanox(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url):
        url = clear_url(url)
        deeplink = ''
        req_url = 'http://toolbox.zanox.com/tools/api/deeplink?' \
                  'connectid={connectid}&' \
                  'format=json&' \
                  'adspaceid={adspaceid}&' \
                  'url={url}' \
            .format(connectid=ZANOX_CONNECT_ID,
                    adspaceid=ZANOX_ADS_SPACE_ID,
                    url=url)
        try:
            r = requests.get(req_url)
            deeplink = r.json()['url']
            if not deeplink:
                logger.error('Error: {}'.format(r.json()))
        except ConnectionError as e:
            logger.error('Error: {}'.format(e))
        return deeplink
