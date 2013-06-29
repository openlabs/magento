Magento Python API
==================

Python library to connect to Magento Webservices.

Check documentation source code

Usage
-----

.. code-block:: python

    import magento

    url = 'http://domain.com/'
    apiuser = 'user'
    apipass = 'password'

    with magento.Product(url, apiuser, apipass) as product_api:
        order_filter = {'created_at':{'from':'2011-09-15 00:00:00'}}
        products = product_api.list(order_filter)

    with magento.ProductTypes(url, apiuser, apipass) as product_type_api:
        product_type = product_type_api.list()
        
    with magento.Product(url, apiuser, apipass) as product_api:
        sku = 'prod1'
        product = product_api.info(sku)

    with magento.API(url, apiuser, apipass) as magento_api:
        # Calling custom APIs if you have extension modules on your
        # magento installation
        websites = magento_api.call('ol_websites.list', [])
        store_group = magento_api.call('ol_groups.list', [])
        store_views = magento_api.call('ol_storeviews.list', [])

    with magento.Order(url, apiuser, apipass) as order_api:
        order_increment_id = '100000001 '
        status = 'canceled'
        order_api.addcomment(order_increment_id, status)

    with magento.Store(url, apiuser, apipass) as store_api:
        store_id = '1'
        store_view_info = store_api.info(store_id)
        store_views = store_api.list()

     with magento.Magento(url, apiuser, apipass) as magento_api:
        magento_info = magento_api.info()


License
-------

GNU Affero General Public License version 3

See LICENSE for more details
