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


class CartCoupon(API):
    """
    Allows you to add and remove coupon codes for a shopping cart.
    """
    __slots__ = ()

    def add(self, quote_id, coupon_code, store_view=None):
        """
        Add a coupon code to a quote.

        :param quote_id: Shopping cart ID (quote ID)
        :param coupon_code, string, Coupon code
        :param store_view: Store view ID or code
        :return: boolean, True if the coupon code is added
        """
        return bool(
            self.call('cart_coupon.add', [quote_id, coupon_code, store_view])
        )

    def remove(self, quote_id, store_view=None):
        """
        Remove a coupon code from a quote

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :return: boolean, True if the coupon code is removed
        """
        return bool(
            self.call('cart_coupon.remove', [quote_id, store_view])
        )


class CartCustomer(API):
    """
    Allows you to add customer information and addresses into a shopping cart.
    """
    __slots__ = ()

    def addresses(self, quote_id, address_data, store_view=None):
        """
        Add customer information into a shopping cart

        :param quote_id: Shopping cart ID (quote ID)
        :param address_data, list of dicts of address details, example
            [
                {
                    'mode': 'billing',
                    'address_id': 'customer_address_id'
                },
                {
                    'mode': 'shipping',
                    'firstname': 'testFirstname',
                    'lastname': 'testLastname',
                    'company': 'testCompany',
                    'street': 'testStreet',
                    'city': 'testCity',
                    'region': 'testRegion',
                    'region_id': 'testRegionId',
                    'postcode': 'testPostcode',
                    'country_id': 'id',
                    'telephone': '0123456789',
                    'fax': '0123456789',
                    'is_default_shipping': 0,
                    'is_default_billing': 0
                },
            ]
        :param store_view: Store view ID or code
        :return: boolean, True if the address is set
        """
        return bool(
            self.call('cart_customer.addresses',
                [quote_id, address_data, store_view])
        )

    def set(self, quote_id, customer_data, store_view=None):
        """
        Add customer information into a shopping cart

        :param quote_id: Shopping cart ID (quote ID)
        :param customer_data, dict of customer details, example
            {
                'firstname': 'testFirstname',
                'lastname': 'testLastName',
                'email': 'testEmail',
                'website_id': '0',
                'store_id': '0',
                'mode': 'guest'
            }
        :param store_view: Store view ID or code
        :return: boolean, True if information added
        """
        return bool(
            self.call('cart_customer.set',
                [quote_id, customer_data, store_view])
        )


class CartPayment(API):
    """
    Allows you to retrieve and set payment methods for a shopping cart.
    """
    __slots__ = ()

    def list(self, quote_id, store_view=None):
        """
        Get the list of available payment methods for a shopping cart

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :return: list of dicts, example
            [{
                'code': 'payment method code',
                'title': 'payment method title',
                'cctypes': ['cc_type1', 'cc_type2', ...],
            }]

        """
        return self.call('cart_payment.list', [quote_id, store_view])

    def method(self, quote_id, payment_data, store_view=None):
        """
        Allows you to set a payment method for a shopping cart (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param payment_data, dict of payment details, example
            {
                'po_number': '',
                'method': 'checkmo',
                'cc_cid': '',
                'cc_owner': '',
                'cc_number': '',
                'cc_type': '',
                'cc_exp_year': '',
                'cc_exp_month': ''
            }
        :param store_view: Store view ID or code
        :return: boolean, True on success
        """
        return bool(
            self.call('cart_payment.method',
                [quote_id, payment_data, store_view])
        )


class CartProduct(API):
    """
    Allows you to manage products in a shopping cart.
    """
    __slots__ = ()

    def add(self, quote_id, product_data, store_view=None):
        """
        Allows you to add one or more products to the shopping cart (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param product_data, list of dicts of product details, example
            [
                {
                    'product_id': 1,
                    'qty': 2,
                    'options': {
                        'option_1': 'value_1',
                        'option_2': 'value_2',
                        ...
                    },
                    'bundle_option': {},
                    'bundle_option_qty': {},
                    'links': [],
                },
                {
                    'sku': 'S0012345',
                    'qty': 4,
                },
            ]
        :param store_view: Store view ID or code
        :return: boolean, True on success (if the product is added to the
                shopping cart)
        """
        return bool(
            self.call('cart_product.add', [quote_id, product_data, store_view])
        )

    def list(self, quote_id, store_view=None):
        """
        Allows you to retrieve the list of products in the shopping cart (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :return: list of dicts, example
            [{
                'product_id': 12345,
                'sku': 'S00012345,
                'name': 'Product Name',
                'set':  1,
                'type': 'Product type',
                'category_ids: [category_id1, ...],
                'website_ids: [website_id1, ...],
            }]

        """
        return self.call('cart_product.list', [quote_id, store_view])

    def move_to_customer_quote(self, quote_id, product_data, store_view=None):
        """
        Allows you to move products from the current quote to a customer quote.

        :param quote_id: Shopping cart ID (quote ID)
        :param product_data, list of dicts of product details, example
            [
                {
                    'product_id': 1,
                    'qty': 2,
                    'options': {
                        'option_1': 'value_1',
                        'option_2': 'value_2',
                        ...
                    },
                    'bundle_option': {},
                    'bundle_option_qty': {},
                    'links': [],
                },
                {
                    'sku': 'S0012345',
                    'qty': 4,
                },
            ]
        :param store_view: Store view ID or code
        :return: boolean, True if the product is moved to customer quote
        """
        return bool(
            self.call('cart_product.moveToCustomerQuote',
                [quote_id, product_data, store_view])
        )

    #: A proxy for :meth:`move_to_customer_quote`
    moveToCustomerQuote = move_to_customer_quote

    def remove(self, quote_id, product_data, store_view=None):
        """
        Allows you to remove one or several products from a shopping cart
        (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param product_data, list of dicts of product details, see def add()
        :param store_view: Store view ID or code
        :return: boolean, True if the product is removed
        """
        return bool(
            self.call('cart_product.remove',
                [quote_id, product_data, store_view])
        )

    def update(self, quote_id, product_data, store_view=None):
        """
        Allows you to update one or several products in the shopping cart
        (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param product_data, list of dicts of product details, see def add()
        :param store_view: Store view ID or code
        :return: boolean, True if the product is updated .
        """
        return bool(
            self.call('cart_product.update',
                [quote_id, product_data, store_view])
        )


class CartShipping(API):
    """
    Allows you to retrieve and set shipping methods for a shopping cart.
    """
    __slots__ = ()

    def list(self, quote_id, store_view=None):
        """
        Allows you to retrieve the list of available shipping methods for a
        shopping cart (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param store_view: Store view ID or code
        :return: list of strings, shipping method codes
        """
        return self.call('cart_shipping.list', [quote_id, store_view])

    def method(self, quote_id, shipping_method, store_view=None):
        """
        Allows you to set a shipping method for a shopping cart (quote).

        :param quote_id: Shopping cart ID (quote ID)
        :param shipping_method, string, shipping method code
        :param store_view: Store view ID or code
        :return: boolean, True if the shipping method is set
        """
        return bool(
            self.call('cart_shipping.method',
                [quote_id, shipping_method, store_view])
        )
