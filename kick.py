# -*- encoding: utf-8 -*-
import cgi
import threading
import os
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from SpiderThread import SpiderThread
from SingleThread import SingleThread

class MainPage(webapp.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user: pass
        else: self.redirect(users.create_login_url(self.request.uri))

        nk225_query = NK225.all().order('-date')
        nk225s = nk225_query.fetch(10)

        template_values = { 'nk225s' : nk225s }
        path = os.path.join(os.path.dirname(__file__), 'nk225getter.html')
        self.response.out.write(template.render(path, template_values))

class CsvOut(webapp.RequestHandler):
    def get(self):
        self.post()

    def post(self):
        threads = {'ScrapingYahoo' : 'http://quote.yahoo.co.jp/'}
        f = os.open('ScrapingYahoo', 'r+')
        f.close()
        self.response.headers['Content-Type'] = 'text/plain'
        for i in threads :
            SpiderThread( i, threads[ i ] )
        self.redirect('/')

class SingleScraping(webapp.RequestHandler):
    def get(self):
        post()

    def post( self ):
        act = self.request.get('action')
        num = self.request.get('last')
        if act=='get':
            c = SingleThread()
            map = c.doOperation()
            n2 = NK225()
            n2.nk225 = map['nk225']
            n2.nk225f = map['nk225f']
            n2.updatedate = map['updatedate']
            n2.put()
        self.redirect('/')

class NK225( db.Model ) :
    date = db.DateTimeProperty(auto_now_add=True)
    updatedate = db.StringProperty(multiline=False)
    nk225 = db.StringProperty(multiline=False)
    nk225f = db.StringProperty(multiline=False)

def main():
    application = webapp.WSGIApplication([
        ('/', MainPage),
        ('/ss', SingleScraping),
        ('/csvout', CsvOut)
        ],debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
