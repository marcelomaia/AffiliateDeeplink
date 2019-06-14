import logging
from urllib import parse

import requests

from .base import BaseDeeplinkGenerator
from .config import AFILIO_TOKEN, AFILIO_AFFID, AFILIO_SITE_ID
from .config import afilio_programs
from .utils import clear_url

logger = logging.getLogger('deeplink.afilio')


class Afilio(BaseDeeplinkGenerator):
    """
    More info at: http://v2.afilio.com.br/Manual/manuais-v2.html
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        deeplink = ''
        try:
            response = cls._req_afilio(url)
            deeplink = response.split('href="')[1].split('" target="')[0].replace('&amp;', '&')
        except IndexError as e:
            logger.error('Error: {}'.format(response))
        except ConnectionError as e:
            logger.error('Error: {}'.format(e))
        return deeplink

    @classmethod
    def _req_afilio(cls, url):
        parsed_uri = parse.urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri).replace('www.', '')
        url = clear_url(url)
        url = parse.quote_plus(url)
        req_url = "http://v2.afilio.com.br/api/deeplink.php" \
                  "?token={token}&affid={affid}&progid={progid}" \
                  "&bantitle=deeplink&bandesc=deeplink&siteid={siteid}" \
                  "&desturl={url}".format(url=url,
                                          progid=afilio_programs.get(domain),
                                          affid=AFILIO_AFFID,
                                          token=AFILIO_TOKEN,
                                          siteid=AFILIO_SITE_ID)
        r = requests.get(req_url)
        return r.text

    @classmethod
    def get_sales_report(cls, start_date, end_date, **kwargs):
        req_url = "http://v2.afilio.com.br/api/leadsale_api.php?" \
                  "mode=list&" \
                  "token={token}&" \
                  "affid={affid}&" \
                  "type=sale&" \
                  "dateStart={start_date}&" \
                  "dateEnd={end_date}&" \
                  "format=JSON".format(token=AFILIO_TOKEN,
                                       affid=AFILIO_AFFID,
                                       start_date=start_date,
                                       end_date=end_date)
        try:
            r = requests.get(req_url)
            return r.json()
        except ConnectionError as e:
            logger.error('Error: {}'.format(e))
        return None
