#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    magento 

    Magento API - SOAP

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPLv3, see LICENSE for more details
'''
__version__ = '0.1.0'

__all__ = [
            'API',
            'Customer', 'CustomerGroup', 'CustomerAddress'
            ]

from api import API
from customer import Customer, CustomerGroup, CustomerAddress
