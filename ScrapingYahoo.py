#
# -*- encoding: utf-8 -*-
#P#############################################################################
#
# file name: scraping_quote_yahoo.py
# description: scraping HTML of quote.yahoo.co.jp using BeautifulSoup
#
#############################################################################P#
import re
import urllib2
import time
from BeautifulSoup import BeautifulSoup
from google.appengine.api import urlfetch

class ScrapingYahoo():
    REGULAR_EXPRESSION_OF_DATE = '(Sun|Mon|Tue|Wed|Thu|Fri|Sat)' +\
        ' (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)' +\
        ' [ ,1-3][0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9] JST [1-2][0,9][0-9][0-9]'
    def getSoup(self): return self.soup
    def setSoup(self, _url):
        page = urllib2.urlopen( _url ).read()
        self.soup = BeautifulSoup(unicode(page,'euc-jp','ignore'))
    def delSoup(self): self.soup = None
    soup = property( getSoup, setSoup, None, delSoup )
    def __init__( self, _url ):
        page = urllib2.urlopen(_url).read()
        self.soup = BeautifulSoup(unicode(page,'euc-jp','ignore'))
    def getResults(self, isTest=False):
        return {'nk225': self.getNK225().replace(',',''),
                'nk225f': self.getNK225FT1().replace(',',''),
                'updatedate': self.getUpdateDate(), 'getdate': time.ctime(time.time())}
    def getNK225( self ):#日経平均株価を取得
        return self.soup.find(name='a', href='/q?d=t&s=998407.O').\
            findNext(name='td').\
                findNext(name='small').\
                    findNext(name='b', text=True)
    def getNK225FT1(self):#日経平均先物１限月を取得
        return self.soup.find(name='a', href='/q?d=t&s=5040469.O').\
            findNext(name='td').\
                findNext(name='small').\
                    findNext(name='b', text=True)
    def getUpdateDate( self ):
        comment = self.soup.find(text=re.compile( 'yahoo\.co\.jp uncompressed' ))
        if comment : pass
        else: return
        p = re.compile( self.REGULAR_EXPRESSION_OF_DATE )
        return p.search( comment ).group()

class ScrapingYahooUsingUrlFetch( ScrapingYahoo ):
    def __init__( self, _url ):
        page = urlfetch.fetch( _url ).content
        self.soup = BeautifulSoup(unicode(page,'euc-jp','ignore'))
    def getSoup(self): return self.soup
    def setSoup(self, _url):
        page = urlfetch.fetch( _url ).content
        self.soup = BeautifulSoup(unicode(page,'euc-jp','ignore'))
    def delSoup(self): self.soup = None
    soup = property( getSoup, setSoup, None, delSoup )
