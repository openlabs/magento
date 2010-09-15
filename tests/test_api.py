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
import ConfigParser
from random import choice
from xmlrpclib import Fault

import nose
from nose.plugins.attrib import attr
from nose.tools import with_setup, nottest, raises
from magentonose import mage_settings

from magento import API, Customer, CustomerGroup, CustomerAddress

log = logging.getLogger()

class ExpectedException(Exception):
    "Used when an expected exception is to be raised"
    pass


context = {
    'URL':None,
    'USERNAME':None,
    'PASSWORD':None,
    'VERSION':None,
    'PROTOCOL':None,
    }

@nottest
def load_from_file(file):
    """
    Loads the config using config parser from file
    :param file: Absolute path of file
    """
    config = ConfigParser.RawConfigParser()
    config.readfp(open(file))
    fields = (
                'URL',
                'USERNAME',
                'PASSWORD',
                'VERSION',
                'PROTOCOL'
                )
    data = dict(zip(fields,
                    [config.get('magento', field.lower()) \
                        for field in fields]))
    return data

@nottest
def setup_connection():
    context.update(load_from_file(mage_settings['config']))

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
        customer_data = {
            'firstname':'Sharoon',
            'lastname':'Thomas',
            'email':'sharoon.thomas@openlabs.co.in'
            }
        len_before_create = len(connection.list())
        customer_id = connection.create(customer_data)
        log.info("Customer ID : %s" % customer_id)
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
    with CustomerAddress(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        assert type(connection.list()) == list



if __name__ == '__main__':
    nose.main()

