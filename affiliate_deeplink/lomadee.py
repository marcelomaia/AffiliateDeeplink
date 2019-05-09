import requests

from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.config import LOMADEE_SOURCE_ID


class Lomadee(BaseDeeplinkGenerator):
    """
        See all advertisers https://www.lomadee.com/dashboard/#/advertisers
    """

    @classmethod
    def get_tracking_url(cls, url):
        req_url = 'http://bws.buscape.com/service/createLinks/lomadee/{app_id}/' \
                  '?sourceId={source_id}&format=json&link1={link_1}'. \
            format(source_id=LOMADEE_SOURCE_ID, link_1=url, app_id='3651516a44624e526551453d')
        r = requests.get(req_url)
        return r.json()['lomadeelinks'][0]['lomadeelink']['redirectlink']
