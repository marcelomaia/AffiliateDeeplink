import logging
from urllib import parse
from urllib.parse import urlparse

from affiliate_deeplink.utils import clear_url

from .base import BaseDeeplinkGenerator
from .config import LOMADEE_ACCEPTED_DOMAINS, LOMADEE_SOURCE_ID

log = logging.getLogger(__file__)


class LomadeeException(Exception):
    pass


class Lomadee(BaseDeeplinkGenerator):
    """
    See all advertisers https://www.lomadee.com/dashboard/#/advertisers
    https://developer.lomadee.com/afiliados/deeplink/recursos/criar-deeplink-manual/
    Estrutura do link
        https://redir.lomadee.com/v2/deeplink?url={url}&sourceId={sourceId}
        Parâmetros:
        {url}: É o link da loja que deseja direcionar o usuário.
        Este link deverá ser encodado. Exemplo: https://www.americanas.com.br
        {sourceId}: ID do afiliado (saber mais)
        {mdasc} (opcional): ID do sub-afiliado (saber mais)

        Exemplo:
        https://redir.lomadee.com/v2/deeplink?url=https%3A%2F%2Fwww.americanas.com.br&sourceId=substituir
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc.replace("www.", "")
        if domain not in LOMADEE_ACCEPTED_DOMAINS:
            log.debug(f"domain {domain} not supported yet")
            return ""
        parsed_url = parse.quote_plus(clear_url(url))
        new_url = f"https://redir.lomadee.com/v2/deeplink?url={parsed_url}&sourceId={LOMADEE_SOURCE_ID}"
        log.debug(f"old url: {url}. new url {new_url}")
        return new_url
