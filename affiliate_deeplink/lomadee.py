import logging

import requests

from .base import BaseDeeplinkGenerator
from .config import LOMADEE_SOURCE_ID

logger = logging.getLogger('deeplink.lomadee')


class Lomadee(BaseDeeplinkGenerator):
    """
        See all advertisers https://www.lomadee.com/dashboard/#/advertisers
    """

    # TODO: extract  req_url to be a function, then monkeypatch on test to verify exceptions
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        deeplink = ''
        try:
            json = cls._req_lomadee(url)
            deeplink = json['lomadeelinks'][0]['lomadeelink']['redirectlink']
        except IndexError as e:
            logger.error('Error: {}'.format(json))
        except KeyError as e:
            logger.error('Error: {}'.format(json))
        except ConnectionError as e:
            logger.error('Error: {}'.format(e))
        return deeplink

    @classmethod
    def _req_lomadee(cls, url):
        req_url = 'http://bws.buscape.com/service/createLinks/lomadee/{app_id}/' \
                  '?sourceId={source_id}&format=json&link1={link_1}'. \
            format(source_id=LOMADEE_SOURCE_ID, link_1=url, app_id='3651516a44624e526551453d')
        r = requests.get(req_url)
        return r.json()
