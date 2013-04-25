# -*- coding: UTF-8 -*-
'''
    magento.directory

    Directory Country API for magento

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010 by Openlabs Technologies & Consulting (P) LTD
    :license: AGPLv3, see LICENSE for more details
'''
from magento.api import API


class Country(API):
    """
    Country API to connect to magento
    """
    __slots__ = ()

    def list(self):
        """
        Retreive list of Countries

        :return: List of dictionaries
        """
        return self.call('directory_country.list', [])


class Region(API):
    """
    Region API to connect to magento
    """
    __slots__ = ()

    def list(self, country):
        """
        Retrieve list of regions

        :param country: Country code in ISO2 or ISO3
        :return: List of Dictionaries
        """
        return self.call('directory_region.list', [country])
