class BaseDeeplinkGenerator(object):
    @classmethod
    def get_tracking_url(cls, url):
        raise NotImplementedError
