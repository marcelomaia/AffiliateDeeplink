## What is it?
This package is used to create deeplinks for affiliate marketing.

Currently supported:
 * [Afilio](http://afilio.com.br/)
 * [B2W](https://secure.afiliados.com.br/)
 * [Amazon](https://associados.amazon.com.br/)
 * [MagazineLuiza](https://www.magazinevoce.com.br/)
 * [Natura](https://natura.com.br)
 * [Banggood](https://www.banggood.com)
 * [Lomadee](https://www.lomadee.com/)
 * [Zanox/Awin](https://marketplace.zanox.com/)

## Installation
##### with setup.py
`python setup.py install`
##### with pip
`pip install affiliate-deeplink`


##### Usage
* Setup environment keys
    * AFILIO_AFFID=
    * AFILIO_TOKEN=
    * AFILIO_SITE_ID=
    * BW2_AFL_ID=
    * AMZ_STORE_NAME=
    * MGZ_STORE_NAME=
    * NATURA_CONSULTORIA_NAME=
    * BANGGOOD_REFERENCE_ID=
    * ZANOX_ADS_SPACE_ID=
    * ZANOX_CONNECT_ID=
    * LOMADEE_SOURCE_ID=
* import module and use-it
    * `>>> from affiliate_deeplink.afilio import Afilio`
    * `>>> Afilio.get_tracking_url('url')`