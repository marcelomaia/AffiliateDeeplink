import os
from urllib.parse import quote_plus

import requests
import requests_cache

from base import BaseDeeplinkGenerator

requests_cache.install_cache(os.path.join(os.path.expanduser('~'), '.affiliate_deeplink_cache'))


class Afilio(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url):
        url = quote_plus(url)
        requrl = "http://v2.afilio.com.br/api/deeplink.php" \
                 "?token={token}&affid={affid}&progid={progid}" \
                 "&bantitle=deeplink&bandesc=deeplink&siteid={siteid}" \
                 "&desturl={url}".format(url=url,
                                         progid=1604,
                                         affid=os.getenv('AFILIO_AFFID'),
                                         token=os.getenv('AFILIO_TOKEN'),
                                         siteid=os.getenv('AFILIO_SITE_ID'))
        r = requests.get(requrl)
        return r.text.split('href="')[1].split('" target="')[0].replace('&amp;', '&')
