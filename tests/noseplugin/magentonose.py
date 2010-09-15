#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento Nose Plugin to pass credentials

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPL3, see LICENSE for more details
'''
import logging
from nose.plugins import Plugin

log = logging.getLogger(__name__)
mage_settings = {}

class MagentoNose(Plugin):
    """
    Extend to set the magento specific arguments
    """
    name = 'magento'
    enabled = True

    def options(self, parser, env):
        """
        Register Command Line options
        """
        parser.add_option(
            '--magento-config',
            dest='magento_config',
            default=env.get('MAGENTO_CONFIG'),
            help="Configuration file for magento")


    def configure(self, options, config):
        """
        Configure plug-in.
        """
        mage_settings['config'] = options.magento_config
        log.debug("Settings are at: %s" % options.magento_config)
