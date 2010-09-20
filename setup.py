#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento API

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPLv3, see LICENSE for more details

    A simple to use python library to access the magento API and
    covered by a complete test suite based on Nose tests. Also
    includes a nose plugin to do the tests based on a config
    file.

    Example usage::
    
        from magento import Customer
        url = 'http://yourmagento.com'
        apiuser = 'apiusername'
        apipass = 'password'
        with Customer(url, apiuser, apipass) as customer_api:
            customer_api.list()

    The implemented methods and APIs are from the Core API of 
    magento documented here: 
    
    http://www.magentocommerce.com/support/magento_core_api

'''
from setuptools import setup
import magento

setup(
    name = 'magento',
    version=magento.__version__,
    url='http://openlabs.co.in/projects/python/magento',
    license='GPL',
    author='Sharoon Thomas, Openlabs Technologies',
    author_email='info@openlabs.co.in',
    description='Magento E-Commerce Integration',
    long_description=__doc__,
    packages=['magento'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'suds>=0.3.9',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

