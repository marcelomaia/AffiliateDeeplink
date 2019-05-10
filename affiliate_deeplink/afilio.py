import logging
from urllib import parse

import requests

from .base import BaseDeeplinkGenerator
from .config import AFILIO_TOKEN, AFILIO_AFFID, AFILIO_SITE_ID
from .config import afilio_programs
from .utils import clear_url

logger = logging.getLogger('deeplink.afilio')


class Afilio(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url):
        deeplink = ''
        parsed_uri = parse.urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri).replace('www.', '')
        url = clear_url(url)
        url = parse.quote_plus(url)
        requrl = "http://v2.afilio.com.br/api/deeplink.php" \
                 "?token={token}&affid={affid}&progid={progid}" \
                 "&bantitle=deeplink&bandesc=deeplink&siteid={siteid}" \
                 "&desturl={url}".format(url=url,
                                         progid=afilio_programs.get(domain),
                                         affid=AFILIO_AFFID,
                                         token=AFILIO_TOKEN,
                                         siteid=AFILIO_SITE_ID)
        try:
            r = requests.get(requrl)
            deeplink = r.text.split('href="')[1].split('" target="')[0].replace('&amp;', '&')
        except IndexError as e:
            logger.error('Error: {}'.format(r.text))
        except ConnectionError as e:
            logger.error('Error: {}'.format(e))
        return deeplink
