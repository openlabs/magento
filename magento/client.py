# -*- coding: UTF-8 -*-
'''
    magento.client

    Client API for magento

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) LTD
    :license: BSD, see LICENSE for more details
'''
from threading import RLock

from .api import API
from .catalog import Category, CategoryAttribute, Product, ProductAttribute, \
    ProductAttributeSet, ProductTypes, ProductImages, ProductTierPrice, \
    ProductLinks, ProductConfigurable, Inventory


_missing = []


class api_class_property(object):
    """A function that converts a function into a lazy property.
    The class wrapped is called the first time to retrieve the result
    and then that calculated result is used the next time you access
    the value.

    Works like the one in Werkzeug but has a lock for thread safety.
    """

    def __init__(self, klass, name=None, doc=None):
        self.__name__ = name or klass.__name__
        self.__module__ = klass.__module__
        self.__doc__ = doc or klass.__doc__
        self.klass = klass
        self.lock = RLock()

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        with self.lock:
            value = obj.__dict__.get(self.__name__, _missing)
            if value is _missing:
                value = self.klass(
                    obj.url,
                    obj.username,
                    obj.password,
                    obj.version,
                    True,
                    obj.protocol,
                )
                obj.__dict__[self.__name__] = value.__enter__()
            return value


class Client(API):
    """
    A convenient API which works more closer to the semantics of the WS API
    rather than the with context manager.

    Example usage::

        from magento import Client
        client = Client('http://yourstore.com', 'api username', 'api password')
        client.catalog_category.tree()
        client.catalog_product.list()

    :param url: URL to the magento instance.
                By default the URL is treated as a base url
                of the domain to which the api part of the URL
                is added. If you want to specify the complete
                URL, set the full_url flag as True.
    :param username: API username of the Web services user. Note
                that this is NOT magento admin username
    :param password: API password of the Web services user.
    :param version: The version of magento the connection is being made to.
                    It is recommended to specify this as there could be
                    API specific changes in certain calls. Default value is
                    1.3.2.4
    :param full_url: If set to true, then the `url` is expected to
                be a complete URL
    :param protocol: 'xmlrpc' and 'soap' are valid values
    """

    catalog_category = api_class_property(Category)
    catalog_category_attribute = api_class_property(CategoryAttribute)
    catalog_product = api_class_property(Product)
    catalog_product_attribute = api_class_property(ProductAttribute)
    catalog_product_attribute_set = api_class_property(ProductAttributeSet)
    catalog_product_type = api_class_property(ProductTypes)
    catalog_product_attribute_media = api_class_property(ProductImages)
    catalog_product_attribute_tier_price = api_class_property(ProductTierPrice)
    catalog_product_link = api_class_property(ProductLinks)

    cataloginventory_stock_item = api_class_property(Inventory)

    ol_catalog_product_link = api_class_property(ProductConfigurable)
