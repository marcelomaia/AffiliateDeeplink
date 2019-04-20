## What is it?
This package is used to create deeplinks for affiliate marketing.
Currently it supports only [Afilio](http://afilio.com.br/)

## Installation
##### with setup.py
`python setup.py install`
##### with pip
`pip install affiliate-deeplink`


##### Usage
* Setup environment keys
    * AFILIO_AFFID = ''
    * AFILIO_TOKEN = ''
    * AFILIO_SITE_ID = ''

* import module and use-it
    * `>>> from affiliate_deeplink.afilio import Afilio`
    * `>>> Afilio.get_tracking_url('url')`