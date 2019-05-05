import os

from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.utils import add_url_params


class Amazon(BaseDeeplinkGenerator):
    """
    TODO: handle more parameters
    tag=goog0ef-20
    smid=A1ZZFT5FULY4LN
    ascsubtag=go_1671362860_66503928682_323778975481_pla-797635043272_c_
    tag=neiamartins-20

    ?ie=UTF8
    linkCode=ll1
    tag=cuponomizar-20
    linkId=0c82dc3a6b69cea2b1529b62e91f4c67
    language=pt_BR

    node=16243840011
    linkCode=ll2
    linkId=48668d55484ff92cc9094d7c8897461d

    """
    @classmethod
    def get_tracking_url(cls, url):
        params = {'tag': os.getenv('AMZ_STORE_NAME'),
                  '_encoding': 'UTF8'}
        url = add_url_params(url, params)
        return url
