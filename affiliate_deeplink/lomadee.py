import logging
from urllib import parse
from urllib.parse import urlparse
from .base import BaseDeeplinkGenerator
from .config import LOMADEE_SOURCE_ID
from affiliate_deeplink.utils import clear_url

logger = logging.getLogger('deeplink.lomadee')

ACCEPTED_DOMAINS = ['maxmilhas.com', 'aramis.com.br', 'novaconcursos.com.br', 'dermage.com.br', 'clubemarisol.com',
                    'pt.newchic.com', 'semparar.comassine-promo', 'tabaratotolevando.comcomprar', 'banggood',
                    'catho.comeducacao', 'escalaverde.com.br', 'seja-lev', 'vestibulares.comanhanguera',
                    'vestibular.unoparead.com', 'bugshop.com', 'seubebeprecisa.com.br', 'reppara.com',
                    'estude-ipemigpos-ead', 'cerejasembolo.com', 'pipocaweb.com', 'aureanutrition.com.br',
                    'loja.betec.com', 'zandarastore.com', 'tf.com', 'magazinepagmenos.com', 'segundociclo.com',
                    'descomplica.com', 'colorbrinque.com', 'lojadomecanico.com.br', 'camisariacolombo.com',
                    'amazon.com',
                    'loja.asus.com', 'americanas.com', 'americanas.com.br', 'nike.com', 'netshoes.com.br',
                    'centauro.com',
                    'loja.electrolux.com.br', 'novomundo.com', 'loja.brastemp.com.br', 'pbkids.com',
                    'pagseguro.uol.com', 'travessa.com', 'lomadee.com', 'shoptime.com', 'hangloose.com',
                    'girafa.com.br', 'girafa.com',
                    'mobly.com', 'submarino.com', 'submarino.com.br', 'lenovobr', 'rihappy.com', 'livrariacultura.com',
                    'abouthome.com.br',
                    'loja.consul.com', 'classictennis.com', 'sieno.com', 'zattini.com', 'br.aliexpress', 'natue.com.br',
                    'maniapop.com', 'drogariasaopaulo.com', 'drogariaspacheco.com', 'leveros.com.br',
                    'lojamultilaser.com', 'pneustore.com.br', 'chicorei', 'gearbest', 'schumann.com', 'flytappt-br',
                    'tng.com', 'jocar.com.br', 'nextel.com', 'repassa.com.br', 'portosegurofaz.com',
                    'meuquantum.com.br', 'loja.meupositivo.com.br', 'valejet', 'beline.com.br', 'loja.br.vaio.com',
                    'inboxshoes.com.br', 'hermosocompadre.com.br', 'malwee.com.br', 'parperfeito.comcpx',
                    'centralar.com.br', 'dresslily.com', 'pt.zaful', 'pierrecardin.com', 'millacabelos.com',
                    'clubepaladar.com', 'iridiumlabs.com.br', 'store.pierrecardin.com', 'donacoelha.com',
                    'irobotloja.com', 'ankeroficial.com', 'nutribulletbrasil.com', 'mmplace.com', 'mirage.com',
                    'lojaweego.com ', 'fata.com.br', 'friopecas.com.br', 'kitchenaid.com.br', 'mrdeal.com.br',
                    'passagensaereas.com', 'editorafoco.com.br', '2amgaming', 'zonacerealista.com',
                    'resultadosdigitais', 'nathusbrasil.com', 'darksidebooks.com.br', 'elare.com.br', 'kitled.com.br',
                    'cliquebemestar.com', 'startech.com', 'stoodi.com.br', 'koralle.com.br', 'ordenato.com.br',
                    'viacaoouroeprata.com.br', 'gazin.com', 'vitalatman.com.br', 'veni.com',
                    'ribsolenergiasolar.com.br', 'natufibras.com.br', 'almundo.com.br', 'boxviva.com.br',
                    'amendoasconfeitadas.com.br', 'hostinger.com.br', 'bralingerie.com.br', 'recco.com.br',
                    'cabanamagazine.com', 'klin.com.br', 'nuuvem', 'uitech.com.br', 'cartersoshkosh.com',
                    'doceerva.com', 'barcelopt', 'joico.com', 'hipervarejo.com', 'lojablowback.com', 'rzmshop.com',
                    'impacta', 'altogiro.net/', 'vibracomigo.com', 'organomix.com.br', 'swift.com.br',
                    'sosolingerie.com', 'ultrabikes.com', 'ultrasports.com.br', 'enebabr', 'deans.com',
                    'cpmoffice.com.br', 'gymchef.com ', 'gourmetzinhocomidinhas.com', 'usaflex.com',
                    'maisbaratostore.com.br', 'grupoa.com', 'yori.store/', 'loja.cartaoanimal.com',
                    'suplementosmaisbaratos', 'etna.com', 'chicbest.com', 'shoponline.iorane.com', 'lojadocafe.com',
                    'cavuca.com.br', 'santorioficial.com', 'zalikacosmeticos.com', 'plantei.com', 'multikidsbaby.com',
                    'lojamultikids.com', 'atrioesportes.com', 'pulsesound.com', 'arenawarrior.com', 'shoprvx.com.br',
                    'oferta-dental', 'samsclub', 'nordvpnpt-br', 'notetec.com', 'finanzero.com', 'reservacool.com.br',
                    'leiturinha.com', 'levok.com', 'hfbrazil.com', 'uniformulaonline.com',
                    'positivocasainteligente.com', 'comix.com', 'usecamisetas', 'pollia.com', 'foundit.com',
                    'conoycosmetics', 'megatonsuplementos.com', 'latifundio.com.br', 'guitarpedia.com', 'mobiliata.com',
                    'homeis.com', 'magrelashop.com', 'bugalupa.com', 'eletroalmeida.com', 'livrariaflorence.com',
                    'vitrinecasual.com.br', 'volcom.com', 'vissla.com', 'vhita.com', 'quintadellarte.com',
                    'mundoinfantilstore.com', 'viggore.com', 'health-pet-seguro', 'loja.alfaparfmilano.com',
                    'lojauniversokids', 'ciclic.com', 'e-cotaseguroauto', 'newbeach.com', 'centerbikemaringa.com.br',
                    ]


class LomadeeException(Exception):
    pass


class Lomadee(BaseDeeplinkGenerator):
    """
        See all advertisers https://www.lomadee.com/dashboard/#/advertisers
        https://developer.lomadee.com/afiliados/deeplink/recursos/criar-deeplink-manual/
        Estrutura do link
            https://redir.lomadee.com/v2/deeplink?url={url}&sourceId={sourceId}
            Parâmetros:
            {url}: É o link da loja que deseja direcionar o usuário. Este link deverá ser encodado. Exemplo: https://www.americanas.com.br
            {sourceId}: ID do afiliado (saber mais)
            {mdasc} (opcional): ID do sub-afiliado (saber mais)

            Exemplo:
            https://redir.lomadee.com/v2/deeplink?url=https%3A%2F%2Fwww.americanas.com.br&sourceId=substituir
    """

    @classmethod
    def get_tracking_url(cls, url, **kwargs):
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc.replace('www.', '')
        if domain not in ACCEPTED_DOMAINS:
            logger.error(f'domain {domain} not supported yet')
            return ''
        parsed_url = parse.quote_plus(clear_url(url))
        deeplink = f'https://redir.lomadee.com/v2/deeplink?url={parsed_url}&sourceId={LOMADEE_SOURCE_ID}'
        logger.debug(f'IN {url} OUT {deeplink}')
        return deeplink
