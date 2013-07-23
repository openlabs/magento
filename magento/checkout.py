# -*- coding: UTF-8 -*-
'''
    magento.checkout

    Checkout API for magento
    Allows you to manage shopping carts and the checkout process.

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010 by Openlabs Technologies & Consulting (P) LTD.

    :license: AGPLv3, see LICENSE for more details
'''

from .api import API


class Cart(API):
    """
    Allows you to manage shopping carts.
    """
    __slots__ = ()

    def create(self, store_view=None):
        """
        Create an empty shopping cart (quote).

        :param store_view: Store view ID or code
        :return: integer, ID of the created empty shopping cart
        """
        return self.call('cart.create', [store_view])

    def info(self, quote_id, store_view=None):
        """
        Retrieve full information about the shopping cart (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :return: dict representing shopping cart info
        """
        return self.call('cart.info', [quote_id, store_view])

    def license(self, quote_id, store_view=None):
        """
        Retrieve the website license agreement for the quote according to the
        website (store).

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :return: dict representing shopping cart license
        """
        return self.call('cart.license', [quote_id, store_view])

    def order(self, quote_id, store_view=None, license_id=None):
        """
        Allows you to create an order from a shopping cart (quote).
        Before placing the order, you need to add the customer, customer
        address, shipping and payment methods.

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :param license_id: Website license ID
        :return: string, result of creating order
        """
        return self.call('cart.order', [quote_id, store_view, license_id])

    def totals(self, quote_id, store_view=None):
        """
        Allows you to retrieve total prices for a shopping cart (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :return: dict representing shopping cart totals
        """
        return self.call('cart.totals', [quote_id, store_view])
