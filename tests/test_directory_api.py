#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento Directory API Testing

    Tests the Directory API

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

from .helpers import setup_connection, context
from magento import Country, Region

log = logging.getLogger()

#############################################################
# Directory Testing
#############################################################

@with_setup(setup=setup_connection)
@attr(description='Try to list all the countries', destructive=False)
def test_country():
    with Country(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        countries = connection.list()
        assert type(countries) == list
        log.info("No of countries : %s" % len(countries))
        log.info("Sample Country : %s" % choice(countries))

@with_setup(setup=setup_connection)
@attr(description='Try to list regions of a country', destructive=False)
def test_region():
    with Country(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        countries = connection.list()
    chosen_country = choice(countries)
    log.info("Country Chosen : %s" % chosen_country)
    with Region(
            context['URL'],
            context['USERNAME'],
            context['PASSWORD'],
            context['VERSION'],
            False,
            context['PROTOCOL']) \
        as connection:
        regions = connection.list(chosen_country['country_id'])
        assert type(regions) == list
        log.info('No of Regions :%s' % len(regions))
        log.info('Sample Region :%s' % (
                        regions and choice(regions) or 'No Regions'
                                        )
        )

if __name__ == '__main__':
    nose.main()

