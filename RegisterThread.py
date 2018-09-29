#
# -*- encoding: utf-8 -*-
#P#############################################################################
#
# file name: RegisterThread.py
# description: register queue to Enterprise Information System
#
#############################################################################P#
import sys
import os
import threading
import time
from Queue import Queue
from ScraperThread import ScraperThread
from google.appengine.ext import db

class RegisterThread(threading.Thread, db.Model):
    QUEUE_MAX_SIZE = 100
    lock = threading.Lock()
    flush_size = 0
    className = ''
    args = ''
    thread_number = 0

    def __init__(self, _flush_size, _thread_number, _className, args):
        self.flush_size = _flush_size
        self.thread_number = _thread_number
        self.className = _className
        self.args = args
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        counter = 0
        childQueues = []
        childThreads = []
        while counter < self.flush_size :
            q = Queue( self.QUEUE_MAX_SIZE )
            childQueues.append( q )
            childThreads.append(
                ScraperThread(childQueues[ counter ], self.className, self.args))
            time.sleep( 1.00 )
            counter += 1

        tmp = []
#        f = open('result.csv', 'a')
        for i, t in enumerate( childThreads ):
            tmp.append( childQueues[ i ].get(True) ) # blocking
            t.join()
            for map in tmp[ i ] :
                t_no = db.StringProperty(self.thread_number)
                nk225 = db.StringProperty(map['225'])
                nk225f = db.StringProperty(map['225f'])
                updatedate = db.StringProperty(map['updatedate'])
                getdate = db.StringProperty(map['getdate'])
#                f.write(str('%d,%s,%s,%s,%s\r\n' % (self.thread_number,
#                                          map['225'], map['225f'],
#                                          map['updatedate'], map['getdate'])))
