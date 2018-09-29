#
# -*- encoding: utf-8 -*-
#P#############################################################################
#
# file name: collectNK225.py
# description: scrape quote.yahoo.co.jp
#
#############################################################################P#
import sys
import os
import time
import threading
from ScraperThread import ScraperThread
from RegisterThread import RegisterThread
from ScrapingYahoo import ScrapingYahoo

class SpiderThread( threading.Thread ):
    FLUSH_SIZE = 5.00
    className = ''
    args = ''

    def __init__(self, className, args):
        self.className = className
        self.args = args
        threading.Thread.__init__( self )
        self.setName( className )
        self.start()

    def run(self):
        count=0
        thread_list=[]
        t = None
        fileName = str( '%s.is.runnable' % self.className )
        while os.path.exists( fileName ) :
            thread_list.append(RegisterThread(
                self.FLUSH_SIZE, count, self.className, self.args))
            time.sleep( self.FLUSH_SIZE )
            count += 1
