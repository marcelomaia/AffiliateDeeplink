import requests

from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.config import ZANOX_ADS_SPACE_ID, ZANOX_CONNECT_ID


class Zanox(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url):
        req_url = 'http://toolbox.zanox.com/tools/api/deeplink?' \
                  'connectid={connectid}&' \
                  'format=json&' \
                  'adspaceid={adspaceid}&' \
                  'url={url}' \
            .format(connectid=ZANOX_CONNECT_ID,
                    adspaceid=ZANOX_ADS_SPACE_ID,
                    url=url)
        r = requests.get(req_url)
        return r.json()['url']
