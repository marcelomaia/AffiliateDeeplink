from setuptools import setup

setup(
    name='affiliate_deeplink',
    version='0.1.3',
    packages=['affiliate_deeplink'],
    url='https://github.com/marcelomaia/AffiliateDeeplink',
    license='MIT',
    author='Marcelo Maia',
    author_email='mmaia.cc@gmail.com',
    description='Deeplink generator for affiliate marketing.',
    install_requires=[
        'requests-cache==0.5.0',
        'requests==2.21.0',
    ],
)
