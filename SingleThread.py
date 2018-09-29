# -*- encoding: utf-8 -*-
#P#############################################################################
#
# file name: SingleThread.py
# description: register queue to Enterprise Information System
#
#############################################################################P#
import sys
import os
from ScrapingYahoo import ScrapingYahooUsingUrlFetch
from google.appengine.ext import db

class SingleThread():

    def doOperation( self ):
        c = ScrapingYahooUsingUrlFetch( 'http://quote.yahoo.co.jp/' )
        return c.getResults()
