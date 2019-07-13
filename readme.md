[![Build Status](https://travis-ci.org/marcelomaia/AffiliateDeeplink.svg?branch=master)](https://travis-ci.org/marcelomaia/AffiliateDeeplink)
[![PyPI version](https://badge.fury.io/py/affiliate-deeplink.svg)](https://badge.fury.io/py/affiliate-deeplink)
[![Pypi downloads](https://img.shields.io/pypi/dm/affiliate-deeplink.svg)](https://img.shields.io/pypi/dm/affiliate-deeplink.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/f9a4f9157b86608f527c/maintainability)](https://codeclimate.com/github/marcelomaia/AffiliateDeeplink/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f9a4f9157b86608f527c/test_coverage)](https://codeclimate.com/github/marcelomaia/AffiliateDeeplink/test_coverage)
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
 * [Hotel Urbano](https://www.clubehu.com.br/) 
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
    * HURB_CMP_ID=
* import affiliate_deeplink module and use-it
    * `>>> import affiliate_deeplink as deeplink`
    * `>>> deeplink.Afilio.get_tracking_url('url')`