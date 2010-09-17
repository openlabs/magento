#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento API Testing Helpers

    General Purpose helper functions for testing

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPL3, see LICENSE for more details
'''
import ConfigParser
from nose.tools import nottest
from magentonose import mage_settings


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

