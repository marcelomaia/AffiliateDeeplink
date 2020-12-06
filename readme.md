# Affiliate deeplink

[![Build status](https://circleci.com/gh/marcelomaia/AffiliateDeeplink.svg?style=svg)](https://app.circleci.com/pipelines/github/marcelomaia/AffiliateDeeplink)
[![PyPI version](https://badge.fury.io/py/affiliate-deeplink.svg)](https://badge.fury.io/py/affiliate-deeplink)
[![Pypi downloads](https://img.shields.io/pypi/dm/affiliate-deeplink.svg)](https://img.shields.io/pypi/dm/affiliate-deeplink.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/f9a4f9157b86608f527c/maintainability)](https://codeclimate.com/github/marcelomaia/AffiliateDeeplink/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f9a4f9157b86608f527c/test_coverage)](https://codeclimate.com/github/marcelomaia/AffiliateDeeplink/test_coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

```
        __  __ _ _ _       _
       / _|/ _(_) (_)     | |
  __ _| |_| |_ _| |_  __ _| |_ ___
 / _` |  _|  _| | | |/ _` | __/ _ \
| (_| | | | | | | | | (_| | ||  __/
 \__,_|_| |_| |_|_|_|\__,_|\__\___|


     _                 _ _       _
    | |               | (_)     | |
  __| | ___  ___ _ __ | |_ _ __ | | __
 / _` |/ _ \/ _ \ '_ \| | | '_ \| |/ /
| (_| |  __/  __/ |_) | | | | | |   <
 \__,_|\___|\___| .__/|_|_|_| |_|_|\_\
                | |
                |_|
```

## What is it

This package is used to create deeplinks for affiliate marketing.

Currently supported:

* [Afilio](http://afilio.com.br/)
* [Amazon](https://associados.amazon.com.br/)
* [B2W](https://secure.afiliados.com.br/)
* [Banggood](https://www.banggood.com)
* [Hotel Urbano](https://www.clubehu.com.br/)
* [Lomadee](https://www.lomadee.com/)
* [MagazineLuiza](https://www.magazinevoce.com.br/)
* [Natura](https://natura.com.br)
* [Zanox/Awin](https://marketplace.zanox.com/)

## Installation

### with setup.py

`python setup.py install`

### with pip

`pip install affiliate-deeplink`

### Usage

* Setup environment keys
  * AFILIO_AFFID=
  * AFILIO_SITE_ID=
  * AFILIO_TOKEN=
  * AMZ_STORE_NAME=
  * AWIN_ADS_SPACE_ID=
  * BANGGOOD_REFERENCE_ID=
  * BW2_AFL_ID=
  * HURB_CMP_ID=
  * LOMADEE_SOURCE_ID=
  * MGZ_STORE_NAME=
  * NATURA_CONSULTORIA_NAME=
  * ZANOX_ADS_SPACE_ID=
  * ZANOX_CONNECT_ID=

* import affiliate_deeplink module and use-it
  * `>>> from affiliate_deeplink import Awin`
  * `>>> Awin.get_tracking_url('url')`
