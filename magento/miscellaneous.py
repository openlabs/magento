# -*- coding: utf-8 -*-
"""
    miscellaneous

    This API allows to access additional magento information

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: AGPLv3, see LICENSE for more details.
"""
from magento.api import API


class Store(API):
    """
    This API allows to retrieve information about store views
    """

    __slots__ = ()

    def info(self, store_id):
        """
        Returns information for store view

        :param store_id: ID of store view
        :return: Dictionary containing information about store view
        """
        return self.call('store.info', [store_id])

    def list(self, filters=None):
        """
        Returns list of store views

        :param filters: Dictionary of filters.

               Format :
                   {<attribute>:{<operator>:<value>}}
               Example :
                   {'store_id':{'=':'1'}}
        :return: List of Dictionaries
        """
        return self.call('store.list', [filters])


class Magento(API):
    """
    This API returns information about current magento installation
    """

    __slots__ = ()

    def info(self):
        """
        Returns information about current magento
        """
        return self.call('core_magento.info', [])
