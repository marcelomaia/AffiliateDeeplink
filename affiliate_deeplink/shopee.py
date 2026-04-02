import hashlib
import json
import logging
import time

import requests

from .base import BaseDeeplinkGenerator
from .config import SHOPEE_APP_ID, SHOPEE_APP_SECRET, SHOPEE_ENDPOINT
from .utils import clear_url

log = logging.getLogger(__file__)


class Shopee(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        """
        Generate a Shopee short link using the Affiliate GraphQL API.
        """
        if not SHOPEE_APP_ID or not SHOPEE_APP_SECRET:
            log.debug("Shopee credentials are missing")
            return ""

        try:
            return cls._req_shopee(url, **kwargs)
        except Exception as exc:
            log.debug(f"{url} -> {exc}")
            return ""

    @classmethod
    def _build_body(cls, origin_url, sub_ids=None):
        query = (
            "mutation($originUrl:String!){"
            "generateShortLink(input:{originUrl:$originUrl}){"
            "shortLink"
            "}"
            "}"
        )
        variables = {"originUrl": origin_url}
        if sub_ids:
            query = (
                "mutation($originUrl:String!,$subIds:[String!]){"
                "generateShortLink(input:{originUrl:$originUrl,subIds:$subIds}){"
                "shortLink"
                "}"
                "}"
            )
            variables["subIds"] = sub_ids

        body_obj = {"query": query, "variables": variables}
        payload = json.dumps(body_obj, ensure_ascii=False, separators=(",", ":"))
        return body_obj, payload

    @classmethod
    def _req_shopee(cls, url, **kwargs):
        origin_url = clear_url(url)
        sub_ids = kwargs.get("subIds") or kwargs.get("sub_ids")
        _, payload = cls._build_body(origin_url, sub_ids=sub_ids)
        ts = str(int(time.time()))
        signature = hashlib.sha256(
            f"{SHOPEE_APP_ID}{ts}{payload}{SHOPEE_APP_SECRET}".encode("utf-8")
        ).hexdigest()
        headers = {
            "Authorization": (
                f"SHA256 Credential={SHOPEE_APP_ID}, Timestamp={ts}, Signature={signature}"
            ),
            "Content-Type": "application/json",
        }
        response = requests.post(SHOPEE_ENDPOINT, headers=headers, data=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        if data.get("errors"):
            raise RuntimeError(data["errors"])
        return data["data"]["generateShortLink"]["shortLink"]
