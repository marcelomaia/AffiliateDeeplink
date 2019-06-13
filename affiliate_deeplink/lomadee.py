import logging

import requests

from .base import BaseDeeplinkGenerator
from .config import LOMADEE_SOURCE_ID

logger = logging.getLogger('deeplink.lomadee')


class Lomadee(BaseDeeplinkGenerator):
    """
        See all advertisers https://www.lomadee.com/dashboard/#/advertisers
    """

    @classmethod
    def get_tracking_url(cls, url):
        deeplink = ''
        req_url = 'http://bws.buscape.com/service/createLinks/lomadee/{app_id}/' \
                  '?sourceId={source_id}&format=json&link1={link_1}'. \
            format(source_id=LOMADEE_SOURCE_ID, link_1=url, app_id='3651516a44624e526551453d')
        try:
            r = requests.get(req_url)
            deeplink = r.json()['lomadeelinks'][0]['lomadeelink']['redirectlink']
        except IndexError as e:
            logger.error('Error: {}'.format(r.text))
        except KeyError as e:
            logger.error('Error: {}'.format(r.text))
        except ConnectionError as e:
            logger.error('Error: {}'.format(e))
        return deeplink
