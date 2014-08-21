# -*- coding: UTF-8 -*-
'''
    magento API

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010-2013 by Openlabs Technologies & Consulting (P) LTD
    :license: AGPLv3, see LICENSE for more details
'''
__all__ = [
            'API', 'Store', 'Magento',
            'Customer', 'CustomerGroup', 'CustomerAddress',
            'Country', 'Region',
            'Cart', 'CartCoupon', 'CartCustomer',
            'CartPayment', 'CartProduct', 'CartShipping',
            
            'Category', 'CategoryAttribute', 'Product', 'ProductAttribute',
            'ProductAttributeSet', 'ProductTypes', 'ProductImages',
            'ProductTierPrice', 'ProductLinks', 'ProductConfigurable',
            'Inventory', 'Order', 'Shipment', 'Invoice', '__version__',
            'Client',
            ]

from .api import API
from .client import Client
from .checkout import Cart, CartCoupon, CartCustomer
from .checkout import CartPayment, CartProduct, CartShipping
from .miscellaneous import Store, Magento
from .customer import Customer, CustomerGroup, CustomerAddress
from .directory import Country, Region
from .catalog import Category, CategoryAttribute
from .catalog import Product, ProductAttribute, ProductAttributeSet
from .catalog import ProductTypes, ProductImages, ProductTierPrice
from .catalog import ProductLinks, ProductConfigurable, Inventory
from .sales import Order, Shipment, Invoice
from .version import VERSION as __version__
