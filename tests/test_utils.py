#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    Magento Utils Testing

    Tests the API Utils

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPL3, see LICENSE for more details
'''

import unittest

from magento.utils import expand_url

class UtilsTestCase(unittest.TestCase):

    def setUp(self):
        """
        Load the account details for a demo magento store
        Hopefully Openlabs will set it up
        """
        pass

    def test_0010_expand_url(self):
        """
        Test the expansion options for URL.
        This test might sound funny, but u will come to know
        its need when hosting companies have all kinds of
        wierd configurations for the URL's and you just want 
        to connect
        """
        url = "http://localhost"
        assert expand_url(url, 'soap') == url+'/api/?wsdl'
        assert expand_url(url, 'xmlrpc') == url+'/index.php/api/xmlrpc'
        url = url + "/"
        assert expand_url(url, 'soap') == url+'api/?wsdl'
        assert expand_url(url, 'xmlrpc') == url+'index.php/api/xmlrpc'

if __name__ == '__main__':
    unittest.main()
