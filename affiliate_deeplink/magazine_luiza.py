import logging
from urllib import parse

from .base import BaseDeeplinkGenerator
from .config import MGZ_STORE_NAME
from .utils import remove_query_params

log = logging.getLogger(__file__)
MAGALU_QUERY_BLACKLIST = {"partner_id", "promoter_id"}


class Magalu(BaseDeeplinkGenerator):
    """
    https://www.magazinevoce.com.br/MGZ_STORE_NAME/[...]
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        """
        Converte links Magalu para magazinevoce.com.br/<MGZ_STORE_NAME>/...
        mantendo path e query originais.
        """
        parsed = parse.urlparse(url)
        sanitized_url = remove_query_params(url, MAGALU_QUERY_BLACKLIST)
        sanitized = parse.urlparse(sanitized_url)

        params = parse.parse_qsl(sanitized.query, keep_blank_values=True)
        rebuilt = []
        for key, value in params:
            if key == "deep_link_value" and value:
                value = remove_query_params(value, MAGALU_QUERY_BLACKLIST)
            rebuilt.append((key, value))
        query = parse.urlencode(rebuilt)
        path_parts = [p for p in parsed.path.split("/") if p]

        if parsed.netloc.endswith("magazinevoce.com.br"):
            if path_parts:
                path_parts[0] = MGZ_STORE_NAME
                new_path = "/" + "/".join(path_parts)
            else:
                new_path = f"/{MGZ_STORE_NAME}"
            if parsed.path.endswith("/"):
                new_path += "/"
            return parse.urlunparse(
                (parsed.scheme, "www.magazinevoce.com.br", new_path, "", query, "")
            )

        if parsed.netloc.endswith("magazineluiza.com.br"):
            base_path = parsed.path if parsed.path.startswith("/") else f"/{parsed.path}"
            new_path = f"/{MGZ_STORE_NAME}{base_path}"
            return parse.urlunparse(
                (parsed.scheme, "www.magazinevoce.com.br", new_path, "", query, "")
            )

        return url
