#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    magento.api

    Generic API for magento

    :copyright: (c) 2010 by Sharoon Thomas.
    :license: GPLv3, see LICENSE for more details
'''
from xmlrpclib import ServerProxy
from suds.client import Client

from .utils import expand_url

class API(object):
    """
    Generic API to connect to magento
    """
    __slots__ = (
        'url',
        'username',
        'password',
        'session',
        'client',
        'protocol',
    )

    def __init__(self, url, username, password,
                 version='1.3.2.4', full_url=False, protocol='xmlrpc'):
        """
        :param url: URL to the magento instance.
                    By default the URL is treated as a base url
                    of the domain to which the api part of the URL
                    is added. If you want to specify the complete
                    URL, set the full_url flag as True.
        :param username: API username of the Web services user. Note
                    that this is NOT magento admin username
        :param password: API password of the Web services user.
        :param version: The version of magento the connection is being made to.
                        It is recommended to specify this as there could be
                        API specific changes in certain calls. Default value is
                        1.3.2.4
        :param full_url: If set to true, then the `url` is expected to
                    be a complete URL
        :param protocol: 'xmlrpc' and 'soap' are valid values
        """
        assert protocol in ('xmlrpc', 'soap')
        self.url = full_url and url or expand_url(url, protocol)
        self.username = username
        self.password = password
        self.protocol = protocol
        self.session = None
        self.client = None

    def connect(self):
        """
        Connects to the service
        but does not login. This could be used as a connection test
        """
        if self.protocol == 'xmlrpc':
            self.client = ServerProxy(self.url, allow_none=True)
        else:
            self.client = Client(self.url)

    def __enter__(self):
        """
        Entry point for with statement
        Logs in and creates a session
        """
        if self.client is None:
            self.connect()
        if self.protocol == 'xmlrpc':
            self.session = self.client.login(
                                self.username,
                                self.password)
        else:
            self.session = self.client.service.login(
                                self.username,
                                self.password)
        return self

    def __exit__(self, type, value, traceback):
        """
        Exit point

        Closes session with magento
        """
        if self.protocol == 'xmlrpc':
            self.client.endSession(self.session)
        else:
            self.client.service.endSession(self.session)
        self.session = None

    def call(self, resource_path, arguments):
        """
        Proxy for SOAP call API
        """
        if self.protocol == 'xmlrpc':
            return self.client.call(self.session, resource_path, arguments)
        else:
            return self.client.service.call(self.session,
                                        resource_path, arguments)

    def multiCall(self, calls, options):
        """
        Proxy for multicalls
        """
        if self.protocol == 'xmlrpc':
            return self.client.multiCall(self.session, calls, options)
        else:
            return self.client.service.multiCall(self.session, calls, options)

