#
# -*- encoding: utf-8 -*-
#P#############################################################################
#
# file name: ScraperThread.py
# description: scraping thread
#
#############################################################################P#
import threading
import time
from Queue import Queue
from ScrapingYahoo import ScrapingYahoo

class ScraperThread( threading.Thread ):
    messageQueue = None
    className = ''
    args = ''
    lock = threading.Lock()
    def __init__(self, _messageQueue, _className, _args ):
        self.messageQueue = _messageQueue
        self.className = _className
        self.args = _args
        threading.Thread.__init__( self )
        self.setDaemon( 1 ) #Daemon化
        self.start()

    def run( self ):
        arrNK225=[ self.
            getClassByName(self.className, self.args).getResults() ]
        self.lock.acquire()
        self.messageQueue.put( arrNK225, True )
        self.lock.release()

    def getClassByName(self, className, args):
        if className == 'ScrapingYahoo' :
            return ScrapingYahoo( args )
        else :
            return
