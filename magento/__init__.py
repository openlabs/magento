# -*- coding: UTF-8 -*-
'''
    magento API

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010-2012 by Openlabs Technologies & Consulting (P) LTD
    :license: AGPLv3, see LICENSE for more details
'''
__version__ = '0.1.5dev'

__all__ = [
            'API',
            'Customer', 'CustomerGroup', 'CustomerAddress',
            'Country', 'Region',
            'Category', 'CategoryAttribute', 'Product', 'ProductAttribute',
            'ProductAttributeSet', 'ProductTypes', 'ProductImages',
            'ProductTierPrice', 'ProductLinks', 'ProductConfigurable', 'Inventory',
            'Order', 'Shipment', 'Invoice',
            ]

from api import API
from customer import Customer, CustomerGroup, CustomerAddress
from directory import Country, Region
from catalog import Category, CategoryAttribute
from catalog import Product, ProductAttribute, ProductAttributeSet
from catalog import ProductTypes, ProductImages, ProductTierPrice
from catalog import ProductLinks, ProductConfigurable, Inventory
from sales import Order, Shipment, Invoice
