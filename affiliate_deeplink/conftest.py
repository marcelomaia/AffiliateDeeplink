import os

import pytest

BASEDIR = os.path.dirname(os.path.abspath(__file__))
links = []

with open(os.path.join(BASEDIR, '__tests__', 'links.txt'), 'r') as f:
    lines = f.readlines()
    for line in lines:
        original, expected = line.split(';')
        links.append((original.strip(), expected.strip()))


@pytest.fixture(scope='function', params=links)
def dirty_urls(request):
    return request.param


@pytest.fixture(scope="function", params=[
    ('http://test.com', {'p1': 'foo', 'p2': 'bar'}, 'http://test.com?p1=foo&p2=bar')])
def param_url(request):
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        ('https://www.banggood.com/pt/Original-Xiaomi-miband-3-Heart-Rate-Monitor-Bluetooth-Smart-'
         'Wristband-Bracelet-p-1145408.html?akmClientCountry=BR&utm_campaign=diegolobopitta'
         '&utm_content=suzhentao&p=GR24207032256201610X',
         'https://www.banggood.com/pt/Original-Xiaomi-miband-3-Heart-Rate-Monitor-Bluetooth-Smart-'
         'Wristband-Bracelet-p-1145408.html?p=UFO&akmClientCountry=BR')])
def bangood_url(request):
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        (
                'https://www.americanas.com.br/produto/113998217/micro-ondas-philco-pme25-25-litros-com-tecla-preparo-rapido-prata-espelhado?epar=b2wafiliados&franq=AFL-03-236386&opn=AFLACOM&voltagem=110%20volts',
                'https://www.americanas.com.br/produto/113998217/micro-ondas-philco-pme25-25-litros-com-tecla-preparo-rapido-prata-espelhado?epar=b2wafiliados&franq=UFO&opn=AFLACOM&voltagem=110 volts&hl=lower'),
        (
                'https://www.submarino.com.br/produto/134251340/tv-led-32-lg-32lv300c-awz-full-hd-com-conversor-digital-integrado-1-usb-1-hdmi-modo-hotel-preto?opn=AFLNOVOSUB&epar=b2wafiliados&franq=AFL-03-236386',
                'https://www.submarino.com.br/produto/134251340/tv-led-32-lg-32lv300c-awz-full-hd-com-conversor-digital-integrado-1-usb-1-hdmi-modo-hotel-preto?opn=AFLNOVOSUB&epar=b2wafiliados&franq=UFO&hl=lower'),
        (
                'https://www.shoptime.com.br/produto/51551285/depilador-eletrico-feminino-batom-portatil-recarregavel-bateria-luz-usb?franq=AFL-03-122110',
                'https://www.shoptime.com.br/produto/51551285/depilador-eletrico-feminino-batom-portatil-recarregavel-bateria-luz-usb?franq=UFO&epar=b2wafiliados&hl=lower&opn=AFLSHOP')])
def b2w_url(request):
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        (
                'https://www.amazon.com.br/gp/offer-listing/B07DYRNSMS/ref=as_li_ss_tl?ie=UTF8&linkCode=ll2&tag=cuponomizar-20&linkId=74efcd2eb036a61501ec53ff0f2be5f6&language=pt_BR',
                'https://www.amazon.com.br/gp/offer-listing/B07DYRNSMS/ref=as_li_ss_tl?tag=UFO&_encoding=UTF8&ie=UTF8&linkCode=ll2&language=pt_BR'
        )]
)
def amazon_url(request):
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        (
                'https://www.natura.com.br/p/lapis-longa-duracao-una-1-2g/24304?a=a&consultoria=beautycare&utm_source=afilio&utm_medium=display&utm_campaign=linktexto_home&utm_content=41411&a=a&',
                'https://www.natura.com.br/p/lapis-longa-duracao-una-1-2g/24304?consultoria=UFO&a=a'
        )]
)
def natura_url(request):
    return request.param


@pytest.fixture(
    scope="function",
    params=[
        (
                'https://www.magazinevoce.com.br/magazineoutletbeleza/p/smart-tv-4k-led-60-philco-ptv60f90dswns-wi-fi-hdr-conversor-digital-3-hdmi-2-usb/4028470/',
                'https://www.magazinevoce.com.br/UFO/p/smart-tv-4k-led-60-philco-ptv60f90dswns-wi-fi-hdr-conversor-digital-3-hdmi-2-usb/4028470/'
        )]
)
def magalu_url(request):
    return request.param


@pytest.fixture(scope="function", params=[('http://americanas.com.br', 'https://iuuuupiiii.com')])
def lomadee_url(request):
    return request.param


@pytest.fixture(scope="function", params=[('https://some.invalid.url',
                                           '')])
def lomadee_url_invalid(request):
    return request.param


@pytest.fixture(scope="function", params=[('https://www.carrefour.com.br/',
                                           'http://yahoo!!!!')])
def afilio_url(request):
    return request.param


@pytest.fixture(scope="function", params=[('https://boticario.com.br',
                                           'http://yahoo!!!!')])
def zanox_url(request):
    return request.param


@pytest.fixture(scope="function", params=[('https://some_invalid.url',
                                           '')])
def zanox_invalid_url(request):
    return request.param
