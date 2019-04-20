## What is it?
This package is used to create deeplinks for affiliate marketing.
Currently it supports only [Afilio](http://afilio.com.br/)

## Local installation
`python setup.py install`

##### Usage
* Setup environment keys
    * AFILIO_AFFID = ''
    * AFILIO_TOKEN = ''
    * AFILIO_SITE_ID = ''

* import module and use-it
    * `>>> from affiliate_deeplink.afilio import Afilio`
    * `>>> Afilio.get_tracking_url('url')`