#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento Catalog API Testing

    Tests the Catalog API

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPL3, see LICENSE for more details
'''
from __future__ import with_statement

import string
from random import choice, sample
from xmlrpclib import Fault
from decimal import Decimal

import nose
from nose.plugins.attrib import attr
from nose.tools import with_setup

from .helpers import setup_connection, context
from magento import Category, CategoryAttribute
from magento import Product

log = logging.getLogger()

#############################################################
# Category
#############################################################

@with_setup(setup=setup_connection)
@attr(description='Try to get store and set same store', destructive=False)
def test_category_currentstore():
    with Category(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        current_store = connection.currentStore()
        assert type(current_store) == int
        assert connection.currentStore(current_store) == current_store

@with_setup(setup=setup_connection)
@attr(description='Try to get the category tree', destructive=False)
def test_category_tree():
    with Category(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        tree = connection.tree()
        assert type(tree) == dict
        log.info("Retreived category %s" % tree)

@with_setup(setup=setup_connection)
@attr(description='Test categories on root level', destructive=False)
def test_category_level():
    with Category(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        categories = connection.level(parent_category=1)
        assert type(categories) == list
        assert len(categories) >= 1

@with_setup(setup=setup_connection)
@attr(description='Test create, info, update, move, assignedproducts'
                   ' and delete operations on category', destructive=True)
def test_category_ops():
    with Category(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        connection.client.verbose = True
        name = ''.join(sample(string.letters, 30))
        
        # Create a new category under default_category  #create
        category_id = connection.create(1, {
                'name':name,
                'is_active':True,
                'available_sort_by':'none',
                'default_sort_by':'none'
            })
        log.info("Category created with ID: %s" % category_id) 

        # Get the same info from category               #info
        new_data = connection.info(category_id)
        log.info("Category Info: %s" % new_data)
        assert new_data['name'] == name
        
        # update the name with olbs at end              #update
        connection.update(category_id, {'name': name+'olbs'})

        # move category under default category of id 2  #move
        connection.move(category_id, 2, 1)

        # ensue that assigned products is an empty list #assignedproducts
        connection.assignedproducts(category_id, 1)

        # delete category
        connection.delete(category_id)

###################################################
# Category Attribute
###################################################

@with_setup(setup=setup_connection)
@attr(description='Try to fetch/set current store in Category Attributes', 
      destructive=False)
def test_category_attr_currstore():
    with CategoryAttribute(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        # Fetch the store
        current_store = connection.currentStore()
        assert type(current_store) == int
        # Now set the store
        connection.currentStore(current_store)

@with_setup(setup=setup_connection)
@attr(description='Try to list all Category Attributes', 
      destructive=False)
def test_category_attr_list():
    with CategoryAttribute(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        attributes = connection.list()
        assert type(attributes) == list
        log.info("Category Attributes %s" % attributes)

@with_setup(setup=setup_connection)
@attr(description='Try to list options of a Category Attribute', 
      destructive=False)
def test_category_attr_list():
    with CategoryAttribute(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        attributes = connection.list()
        attribute = choice(attributes)
        while not attribute['attribute_id']:
            attribute = choice(attributes)
        log.info("Chosen Category Attribute: %s" % attribute)
        options = connection.options(attribute['attribute_id'])
        log.info("Attribute options: %s" % options)
        assert type(options) == list

###################################################
# Product
###################################################

@with_setup(setup=setup_connection)
@attr(description='Try to fetch/set current store in Product', 
      destructive=False)
def test_product_currstore():
    with Product(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        # Fetch the store
        current_store = connection.currentStore()
        assert type(current_store) == int
        # Now set the store
        connection.currentStore(current_store)

@with_setup(setup=setup_connection)
@attr(description='Try to list all products', 
      destructive=False)
def test_product_list():
    with Product(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        products = connection.list()
        log.info("Products: %s" % products)
        assert type(products) == list
        if products:
            # Test with filters
            filtered = connection.list({'sku':{'=':products[0]['sku']}})
            assert len(filtered)==1
            assert filtered[0]['sku'] == products[0]['sku']

@with_setup(setup=setup_connection)
@attr(description='Try to get info of a product', 
      destructive=False)
def test_product_info():
    with Product(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        products = connection.list()
        if products:
            product = choice(products)
            log.info("Chosen product: %s" % product)
            # Fetch by SKU
            connection.info(product['sku'])
            # Fetch by ID
            connection.info(product['product_id'])

@with_setup(setup=setup_connection)
@attr(description='Try to create/update/special price/delete a product', 
      destructive=True)
def test_product_create_update_special_delete():
    with Product(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        sku = name = ''.join(sample(string.letters, 30))
        # Create
        product_id = connection.create(
            'simple', 4, sku, {
                'name':sku + 'create'
                }
        )
        assert type(product_id) == int
        # Update
        assert connection.update(sku, {'name':sku + 'update'})
        product = connection.info(sku)
        assert product['name'] == sku + 'update'
        # Special Price
        new_price = choice(range(0,100))
        assert connection.setSpecialPrice(sku, new_price)
        special_price = connection.getSpecialPrice(sku)
        log.info("Special Price: %s" % special_price)
        assert Decimal(special_price['special_price']) == Decimal(str(new_price))
        # Finally delete product
        assert connection.delete(sku)

if __name__ == '__main__':
    nose.main()
