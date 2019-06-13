import requests

from .base import BaseDeeplinkGenerator
from .config import LOMADEE_SOURCE_ID

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}


class Lomadee(BaseDeeplinkGenerator):
    """
        See all advertisers https://www.lomadee.com/dashboard/#/advertisers
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        req_url = 'http://bws.buscape.com/service/createLinks/lomadee/{app_id}/' \
                  '?sourceId={source_id}&format=json&link1={link_1}'. \
            format(source_id=LOMADEE_SOURCE_ID, link_1=url, app_id='3651516a44624e526551453d')
        r = requests.get(req_url, headers=headers)
        return r.json()['lomadeelinks'][0]['lomadeelink']['redirectlink']
