class BaseDeeplinkGenerator(object):
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        raise NotImplementedError

    @classmethod
    def get_sales_report(cls, start_date, end_date, **kwargs):
        raise NotImplementedError
