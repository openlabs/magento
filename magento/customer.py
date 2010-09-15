#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    magento.customer

    Customer API for magento

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPLv3, see LICENSE for more details
'''

from .api import API

class Customer(API):
    """
    Customer API to connect to magento
    """
    __slots__ = ( )

    def list(self, filters=None):
        """
        Retreive list of customers

        :param filters: Dictionary of filters.
            Format :
                `{<attribute>:{<operator>:<value>}}`
            Example :
                `{'firstname':{'ilike':'sharoon'}}`
        :return: List of dictionaries of matching records
        """
        return self.call('customer.list', filters and [filters] or [])

    def create(self, data):
        """
        Create a customer using the given data
        :param data: Dictionary of values
        :return: Integer ID of new record
        """
        return self.call('customer.create', [data])

    def info(self, id, attributes=None):
        """
        Retrieve customer data

        :param id: ID of customer
        :param attributes: `List` of attributes needed
        """
        if attributes:
            return self.call('customer.info', [id, attributes])
        else:
            return self.call('customer.info', [id])

    def update(self, id, data):
        """
        Update a customer using the given data
        :param id: ID of the customer record to modify
        :param data: Dictionary of values
        :return: Boolean
        """
        return self.call('customer.update', [id, data])

    def delete(self, id):
        """
        Delete a customer
        :param id: ID of customer to delete
        :return: Boolean
        """
        return self.call('customer.delete', [id])


class CustomerGroup(API):
    """
    Customer Group API to connect to magento
    """
    __slots__ = ( )

    def list(self):
        """
        Retreive list of customers

        :return: List of dictionaries of matching records
        """
        return self.call('customer_group.list', [])


class CustomerAddress(API):
    """
    Customer Address API
    """
    __slots__ = ()

    def list(self, customer_id):
        """
        Retreive list of customer Addresses

        :param customer_id:ID of customer whose address needs
                            to be fetched
        :return: List of dictionaries of matching records
        """
        return self.call('customer.list', [customer_id])

    def create(self, data):
        """
        Create a customer using the given data
        :param data: Dictionary of values
        :return: Integer ID of new record
        """
        return self.call('customer.create', [data])

    def info(self, id, attributes=None):
        """
        Retrieve customer data

        :param id: ID of customer
        :param attributes: `List` of attributes needed
        """
        if attributes:
            return self.call('customer.info', [id, attributes])
        else:
            return self.call('customer.info', [id])

    def update(self, id, data):
        """
        Update a customer using the given data
        :param id: ID of the customer record to modify
        :param data: Dictionary of values
        :return: Boolean
        """
        return self.call('customer.update', [id, data])

    def delete(self, id):
        """
        Delete a customer
        :param id: ID of customer to delete
        :return: Boolean
        """
        return self.call('customer.delete', [id])
