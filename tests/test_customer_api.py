#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento Utils Testing

    Tests the API Utils

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPL3, see LICENSE for more details
'''
from __future__ import with_statement

import unittest
import logging
from random import choice
from xmlrpclib import Fault

import nose
from nose.plugins.attrib import attr
from nose.tools import with_setup, nottest, raises

from .helpers import setup_connection, context, ExpectedException
from magento import API, Customer, CustomerGroup, CustomerAddress

log = logging.getLogger()

#############################################################
# Customer Tests
#############################################################

@with_setup(setup=setup_connection)
@attr(description='Try to connect to magento Instance', destructive=False)
def test_connection():
    with API(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        log.info("Session ID: %s" % connection.session)
        assert connection.session is not None

@with_setup(setup=setup_connection)
@attr(description='Take a list and see if customer exists', destructive=False)
def test_list_customer():
    with Customer(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        log.info("Customers list %s" % connection.list())

@with_setup(setup=setup_connection)
@attr(description='Try to create a new customer', destructive=True)
def test_create_customer():
    with Customer(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        #Check if customer already exists
        customers = connection.list({'email':{'=':'test@openlabs.co.in'}})
        if customers:
            customer_id = customers[0]['customer_id']
            log.info('Customer already exists, so delete %s' % customer_id)
            connection.delete(customer_id)
        customer_data = {
            'firstname':'Sharoon',
            'lastname':'Thomas',
            'email':'test@openlabs.co.in'
            }
        len_before_create = len(connection.list())
        customer_id = connection.create(customer_data)
        log.info("Customer ID : %s Type:%s" % ( customer_id,
                                                type(customer_id)
                                                )
        )
        len_after_create = len(connection.list())
        assert type(customer_id) in (int, long)
        assert len_after_create > len_before_create

@with_setup(setup=setup_connection)
@attr(description='Try to update an existing customer and get info',
        destructive=True)
def test_update_customer():
    with Customer(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:

        existing_customers = connection.list()
        if not existing_customers:
            raise Exception("No existing customers to modify")
        #Choose a customer from existing list
        customer = choice(existing_customers)
        #Change first name and update
        firstname = "testfirst"
        connection.update(customer['customer_id'], {'firstname':firstname})
        #Read the same customer and check if first name is same
        updated_customer = connection.info(customer['customer_id'])
        assert updated_customer['firstname'] == firstname

@raises(ExpectedException)
@with_setup(setup=setup_connection)
@attr(description='Try to delete a newly created customer',
        destructive=True)
def test_delete_customer():
    with Customer(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        id = connection.create({
            'firstname':'ToDelete',
            'lastname':'ToDelete',
            'email':'delete@openlabs.co.in'
        })
        connection.delete(id)
        #Try to delete again, and assert the exception in decorator
        try:
            connection.delete(id)
        except Fault, fault:
            if fault.faultCode == 102: #Customer not exists
                raise ExpectedException(fault)
            else:
                raise fault

#############################################################
# Customer Groups Tests
#############################################################
@with_setup(setup=setup_connection)
@attr(description='Try to list all customer categories',
        destructive=False)
def test_customer_group_list():
    with CustomerGroup(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        assert type(connection.list()) == list

#############################################################
# Customer Address Tests
#############################################################
@with_setup(setup=setup_connection)
@attr(description='Try to list all customer addresses',
        destructive=False)
def test_customer_address_list():
    with Customer(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        customers = connection.list()
    if not customers:
        raise Exception('No customers to test and create address')
    with CustomerAddress(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        assert type(connection.list(
                        customers[0]['customer_id'])
                                    ) == list

@with_setup(setup=setup_connection)
@attr(description='Try to create a new customer addresses and check it',
        destructive=True)
def test_customer_address_create():
    #First get a customer to create address
    with Customer(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        customers = connection.list()
    if not customers:
        raise Exception('No customers to test and create address')
    #Now create address for customer
    with CustomerAddress(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        address_id = connection.create(
            customers[0]['customer_id'],
            {
                'firstname':'testaddress',
                'lastname':'testaddress',
                'street':'street',
                'city':'city',
                'country_id':'GB',
                'region':'Lancashire',
                'postcode':'M145EU',
                'telephone':'0987654321'
                }
            )
        assert type(address_id) in (int, long)
        #now check this info has been updated
        address = connection.info(address_id)
        assert address['firstname'] == 'testaddress'
        assert address['lastname'] == 'testaddress'
        assert address['street'] == 'street'
        assert address['city'] == 'city'

if __name__ == '__main__':
    nose.main()

