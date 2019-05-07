from urllib import parse as url_parse

import requests

from affiliate_deeplink.base import BaseDeeplinkGenerator
from affiliate_deeplink.config import AFILIO_TOKEN, AFILIO_AFFID, AFILIO_SITE_ID

programs = {
    "walmart.com.br": 191,
    "polishop.com.br": 357,
    "centauro.com.br": 382,
    "latam.com": 483,
    "nespresso.com": 1968,
    "shopfato.com.br": 573,
    "netshoes.com.br": 577,
    "cvc.com.br": 610,
    "mobly.com.br": 764,
    "pontofrio.com.br": 768,
    "extra.com.br": 769,
    "casasbahia.com.br": 770,
    "rihappy.com.br": 928,
    "fastshop.com.br": 994,
    "submarino.com.br": 1008,
    "shoptime.com.br": 1009,
    "americanas.com.br": 1010,
    "oqvestir.com.br": 1086,
    "epocacosmeticos.com.br": 1102,
    "thebeautybox.com.br": 1123,
    "lojaskd.com.br": 1134,
    "cantao.com.br": 1171,
    "posthaus.com.br": 1187,
    "livrariacultura.com.br": 1190,
    "onofreagora.com.br": 1222,
    "wine.com.br": 1225,
    "boticario.com.br": 1255,
    "hopelingerie.com.br": 1260,
    "eudora.com.br": 1318,
    "supermuffato.com.br": 1326,
    "quemdisseberenice.com.br": 1329,
    "megamamute.com.br": 1509,
    "offpremium.com.br": 1534,
    "fyistore.com.br": 1536,
    "animale.com.br": 1537,
    "ikesaki.com.br": 1606,
    "divvino.com.br": 2459,
    "divinoamor.com.br": 1601,
    "natura.com.br": 1604,
    "pontofrioatacado.com.br": 1619,
    "trocafone.com": 1672,
    "cea.com.br": 1678,
    "balaodainformatica.com.br": 1681,
    "afabula.com.br": 1701,
    "maccosmetics.com.br": 2253,
    "onofre.com.br": 1719,
    "madeiramadeira.com.br": 1885,
    "colombo.com.br": 1739,
    "emporio.com": 1754,
    "zattini.com.br": 1785,
    "shopfacil.com.br": 1796,
    "sephora.com.br": 1926,
    "mercatto.com.br": 1830,
    "chicorei.com": 1944,
    "taqi.com.br": 1950,
    "friboi.com.br": 1951,
    "bobstore.com.br": 1959,
    "carrefour.com.br": 2001,
    "korresbr.com.br": 2628,
    "loja.jequiti.com.br": 2495,
    "centralar.com.br": 2168,
    'banggood.com': 2693
}


class Afilio(BaseDeeplinkGenerator):
    @classmethod
    def get_tracking_url(cls, url):
        parsed_uri = url_parse.urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri).replace('www.', '')
        url = url_parse.quote_plus(url)
        requrl = "http://v2.afilio.com.br/api/deeplink.php" \
                 "?token={token}&affid={affid}&progid={progid}" \
                 "&bantitle=deeplink&bandesc=deeplink&siteid={siteid}" \
                 "&desturl={url}".format(url=url,
                                         progid=programs.get(domain),
                                         affid=AFILIO_AFFID,
                                         token=AFILIO_TOKEN,
                                         siteid=AFILIO_SITE_ID)
        r = requests.get(requrl)
        return r.text.split('href="')[1].split('" target="')[0].replace('&amp;', '&')
