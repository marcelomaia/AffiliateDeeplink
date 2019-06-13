import logging
from json import dumps
from urllib import parse
from urllib.parse import (unquote, urlparse, parse_qsl, ParseResult)

log = logging.getLogger('deeplink.util')


def add_url_params(url, params):
    """ Add GET params to provided URL being aware of existing.

    :param url: string of target URL
    :param params: dict containing requested params to be added
    :return: string with updated URL

    >> url = 'http://stackoverflow.com/test?answers=true'
    >> new_params = {'answers': False, 'data': ['some','values']}
    >> add_url_params(url, new_params)
    'http://stackoverflow.com/test?data=some&data=values&answers=false'
    """
    # Unquoting URL first so we don't loose existing args
    url = unquote(url)
    # Extracting url info
    parsed_url = urlparse(url)
    # Extracting URL arguments from parsed URL
    get_args = parsed_url.query
    # Converting URL arguments to dict
    parsed_get_args = dict(parse_qsl(get_args))
    # Merging URL arguments dict with new params
    parsed_get_args.update(params)

    # Bool and Dict values should be converted to json-friendly values
    # you may throw this part away if you don't like it :)
    parsed_get_args.update(
        {k: dumps(v) for k, v in parsed_get_args.items()
         if isinstance(v, (bool, dict))}
    )
    # Converting URL argument to proper query string
    query_args = '&'.join([('{}={}'.format(p, q)) for p, q in parsed_get_args.items()])
    # Creating new parsed result object based on provided with new
    # URL arguments. Same thing happens inside of urlparse.
    new_url = ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path,
        parsed_url.params, query_args, parsed_url.fragment
    ).geturl()

    return new_url


ignore_args = ['tag', 'ref', 'linkId',  # amazon
               'p', 'utm_campaign', 'utm_content', 'custlinkid',  # bangood
               'utm_source', 'zanpid', 'utm_medium', 'utm_campaign', 'origem',  # zanox
               'utm_term', 'siteID', 'utm_source', 'utm_medium', 'u1',  # rakuten
               'ranMID', 'utm_term', 'ranSiteID', 'IdParceiro',  # rakuten
               'lmdsid',  # lomadee
               ]


def clear_url(url: str, input_params: dict = {}) -> str:
    """
    :param url: some affiliate link supported
    :param input_params: {data:value}
    :return:
    """
    params = {}
    params.update(input_params)
    parsed_uri = parse.urlparse(url)
    params_dict = dict(parse.parse_qsl(parsed_uri.query))
    for key in params_dict:
        if key not in ignore_args:
            params[key] = params_dict[key]
    cleared_url = '{scheme}://{netloc}{path}'.format(scheme=parsed_uri.scheme,
                                                     netloc=parsed_uri.netloc,
                                                     path=parsed_uri.path)
    cleared_url = add_url_params(cleared_url, params)
    log.debug('URL cleared, \nfrom {} \nto {}'.format(url, cleared_url))
    return cleared_url
