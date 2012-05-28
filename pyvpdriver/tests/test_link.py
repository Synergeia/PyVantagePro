# coding: utf8
'''
    pyvpdriver.tests.test_link
    --------------------------

    :copyright: Copyright 2012 Salem Harrache and contributors, see AUTHORS.
    :license: GNU GPL v3.

'''

from __future__ import division, unicode_literals

from ..link import TCPLink

class TestTCPLink:

    def setup_class(self):
        """Setup common data."""
        # echo service
        self.link = TCPLink('localhost', 7)

    def test_hello_echo(self):
        """Test echo."""
        self.link.write("hello")
        assert self.link.read(5) == "hello"
