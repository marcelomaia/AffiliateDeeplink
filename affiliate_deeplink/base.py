import os

import requests_cache

requests_cache.install_cache(os.path.join(os.path.expanduser('~'), '.affiliate_deeplink_cache'))


class BaseDeeplinkGenerator(object):
    @classmethod
    def get_tracking_url(cls, url):
        raise NotImplementedError
