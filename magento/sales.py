# -*- coding: UTF-8 -*-
'''
    magento.sales

    Allows to export/import sales orders from/into Magento,
    to create invoices, shipments, credit memos

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010-2013 by Openlabs Technologies & Consulting (P) LTD
    :license: AGPLv3, see LICENSE for more details
'''
from .api import API


class Order(API):
    """
    Allows to import/export orders.
    """
    __slots__ = ()

    def list(self, filters=None):
        """
        Retrieve order list by filters

        :param filters: Dictionary of filters.

               Format :
                   `{<attribute>:{<operator>:<value>}}`
               Example :
                   `{'firstname':{'ilike':'sharoon'}}`

        :return: `list` of `dict`
        """
        return self.call('sales_order.list', [filters])

    def search(self, filters=None, fields=None, limit=None, page=1):
        """
        Retrieve order list by options using search api. Using this result can
        be paginated

        :param options: Dictionary of options.

        :param filters: `{<attribute>:{<operator>:<value>}}`
        :param fields: [<String: magento field names>, ...]
        :param limit: `page limit`
        :param page: `current page`

        :return: `list` of `dict`
        """
        options = {
            'imported': False,
            'filters': filters or {},
            'fields': fields or [],
            'limit': limit or 1000,
            'page': page,
        }
        return self.call('sales_order.search', [options])

    def info(self, order_increment_id):
        """
        Retrieve order info

        :param order_increment_id: Order ID
        """
        return self.call(
            'sales_order.info', [order_increment_id]
            )

    def addcomment(self, order_increment_id,
            status, comment=None, notify=False):
        """
        Add comment to order or change its state

        :param order_increment_id: Order ID
        TODO: Identify possible values for status
        """
        if comment is None:
            comment = ""
        return bool(self.call(
                'sales_order.addComment',
                [order_increment_id, status, comment, notify]
            )
        )

    #: A proxy for :meth:`addcomment`
    addComment = addcomment

    def hold(self, order_increment_id):
        """
        Hold order

        :param order_increment_id: Order ID
        """
        return bool(self.call('sales_order.hold', [order_increment_id]))

    def unhold(self, order_increment_id):
        """
        Unhold order

        :param order_increment_id: Order ID
        """
        return bool(self.call('sales_order.unhold', [order_increment_id]))

    def cancel(self, order_increment_id):
        """
        Cancel an order

        :param order_increment_id: Order ID
        """
        return bool(self.call('sales_order.cancel', [order_increment_id]))


class Shipment(API):
    """
    Allows create/export order shipments.
    """
    __slots__ = ()

    def list(self, filters=None):
        """
        Retrieve shipment list by filters

        :param filters: Dictionary of filters.

               Format :
                   `{<attribute>:{<operator>:<value>}}`
               Example :
                   `{'firstname':{'ilike':'sharoon'}}`

        :return: `list` of `dict`
        """
        return self.call('sales_order_shipment.list', [filters])

    def info(self, shipment_increment_id):
        """
        Retrieve shipment info

        :param shipment_increment_id: Order ID
        """
        return self.call('sales_order_shipment.info', [shipment_increment_id])

    def create(self, order_increment_id,
            items_qty, comment=None, email=True, include_comment=False):
        """
        Create new shipment for order

        :param order_increment_id: Order Increment ID
        :type order_increment_id: str
        :param items_qty: items qty to ship
        :type items_qty: associative array (order_item_id ⇒ qty) as dict
        :param comment: Shipment Comment
        :type comment: str
        :param email: send e-mail flag (optional)
        :type email: bool
        :param include_comment: include comment in e-mail flag (optional)
        :type include_comment: bool
        """
        if comment is None:
            comment = ''
        return self.call(
            'sales_order_shipment.create', [
                order_increment_id, items_qty, comment, email, include_comment
            ]
        )

    def addcomment(self, shipment_increment_id,
            comment, email=True, include_in_email=False):
        """
        Add new comment to shipment

        :param shipment_increment_id: Shipment ID
        """
        return bool(
            self.call(
                'sales_order_shipment.addComment',
                [shipment_increment_id, comment, email, include_in_email]
            )
        )

    #: A proxy for :meth:`addcomment`
    addComment = addcomment

    def addtrack(self, shipment_increment_id, carrier, title, track_number):
        """
        Add new tracking number

        :param shipment_increment_id: Shipment ID
        :param carrier: Carrier Code
        :param title: Tracking title
        :param track_number: Tracking Number
        """
        return self.call(
            'sales_order_shipment.addTrack',
            [shipment_increment_id, carrier, title, track_number]
        )

    #: A proxy for :meth:`addtrack`
    addTrack = addtrack

    def removetrack(self, shipment_increment_id, track_id):
        """
        Remove tracking number

        :param shipment_increment_id: SHipment ID
        :param track_id: Tracking number to remove
        """
        return bool(
            self.call(
                'sales_order_shipment.removeTrack',
                [shipment_increment_id, track_id]
            )
        )

    #: A proxy for :meth:`removetrack`
    removeTrack = removetrack

    def getcarriers(self, order_increment_id):
        """
        Retrieve list of allowed carriers for order

        :param order_increment_id: Order ID
        """
        return self.call(
            'sales_order_shipment.getCarriers', [order_increment_id]
        )

    #: A proxy for :meth:`getcarriers`
    getCarriers = getcarriers

    def sendinfo(self, shipment_increment_id, comment=''):
        """
        Send email with shipment data to customer

        :param order_increment_id: Order ID
        """
        return self.call(
            'sales_order_shipment.sendInfo', [shipment_increment_id, comment]
        )

    #: A proxy for :meth:`sendinfo`
    sendInfo = sendinfo


class Invoice(API):
    """
    Allows create/export order invoices
    """
    __slots__ = ()

    def list(self, filters=None):
        """
        Retrieve invoice list by filters

        :param filters: Dictionary of filters.

               Format :
                   `{<attribute>:{<operator>:<value>}}`
               Example :
                   `{'firstname':{'ilike':'sharoon'}}`

        :return: `list` of `dict`
        """
        return self.call('sales_order_invoice.list', [filters])

    def info(self, invoice_increment_id):
        """
        Retrieve invoice info

        :param invoice_increment_id: Invoice ID
        """
        return self.call(
            'sales_order_invoice.info', [invoice_increment_id]
        )

    def create(self, order_increment_id, items_qty,
            comment=None, email=True, include_comment=False):
        """
        Create new invoice for order

        :param order_increment_id: Order increment ID
        :type order_increment_id: str
        :param items_qty: Items quantity to invoice
        :type items_qty: dict
        :param comment: Invoice Comment
        :type comment: str
        :param email: send invoice on e-mail
        :type email: bool
        :param include_comment: Include comments in email
        :type include_comment: bool

        :rtype: str
        """
        return self.call(
            'sales_order_invoice.create',
            [order_increment_id, items_qty, comment, email, include_comment]
        )

    def addcomment(self, invoice_increment_id,
            comment=None, email=False, include_comment=False):
        """
        Add comment to invoice or change its state

        :param invoice_increment_id: Invoice ID
        """
        if comment is None:
            comment = ""
        return bool(
            self.call(
                'sales_order_invoice.addComment',
                [invoice_increment_id, comment, email, include_comment]
            )
        )

    #: Add a proxy for :meth:`addcomment`
    addComment = addcomment

    def capture(self, invoice_increment_id):
        """
        Capture Invoice

        :attention: You should check the invoice to see if can be
        captured before attempting to capture an invoice, otherwise
        the API call with generate an error.

        Invoices have states as defined in the model
        Mage_Sales_Model_Order_Invoice:

        STATE_OPEN = 1
        STATE_PAID = 2
        STATE_CANCELED = 3

        Also note there is a method call in the model that checks this
        for you canCapture(), and it also verifies that the payment is
        able to be captured, so the invoice state might not be the only
        condition that’s required to allow it to be captured.

        :param invoice_increment_id: Invoice ID
        :rtype: bool
        """
        return bool(
            self.call('sales_order_invoice.capture', [invoice_increment_id])
        )

    def void(self, invoice_increment_id):
        """
        Void an invoice

        :param invoice_increment_id: Invoice ID
        :rtype: bool
        """
        return bool(
            self.call('sales_order_invoice.void', [invoice_increment_id])
        )

    def cancel(self, invoice_increment_id):
        """
        Cancel invoice

        :param invoice_increment_id: Invoice ID
        :rtype: bool
        """
        return bool(
            self.call('sales_order_invoice.cancel', [invoice_increment_id])
        )
