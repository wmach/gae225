#
# -*- encoding: utf-8 -*-
#P#############################################################################
#
# file name: SpinderMainThread.py
# description: main thread not daemon
#
#############################################################################P#
import threading
from SpiderThread import SpiderThread

#url = 'file:///C:/2008/html/quote.yahoo.co.jp.html
#url = 'file:///C:/Documents and Settings/mwarashina/My Documents/2008/html/dummy.quote.yahoo.co.jp.html'

threads = {\
'ScrapingYahoo' : 'http://quote.yahoo.co.jp/' \
          }

for i in threads :
    SpiderThread( i, threads[ i ] )

