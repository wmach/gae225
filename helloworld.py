# -*- encoding: utf-8 -*-
import cgi
import wsgiref.handlers
import threading
import os
from SpiderThread import SpiderThread
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db

class MainPage(webapp.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
             pass
#            self.response.headers['Content-Type'] = 'text/plain'
#            self.response.out.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

        self.response.out.write('<html><body>')
        greetings = db.GqlQuery("SELECT * FROM Greeting ORDER BY date DESC LIMIT 10")
        wao = db.GqlQuery("SELECT * FROM RegisterThread ORDER BY date DESC LIMIT 10")
        for greeting in greetings:
            if greeting.author:
                self.response.out.write('<b>%s</b> wrote:' % greeting.author.nickname())
            else :
                self.response.out.write('An anonymous person wrote:')
            self.response.out.write('<blockquote>%s</blockquote>' %
                cgi.escape(greeting.content))
        for w in wao:
            if w.t_no:
                self.response.out.write('%s' % w.t_no)
            elif w.nk225:
                self.response.out.write('%s' % w.nk225)
            elif w.nk225f:
                self.response.out.write('%s' % w.nk225f)
            elif w.updatedate:
                self.response.out.write('%s' % w.updatedate)
            elif w.getdate:
                self.response.out.write('%s' % w.getdate)

        # Write the submission from and the footer of the page
        self.response.out.write("""
            <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="please sign"></div>
            </form>
            </body></html>""")

#        self.response.out.write("""
#            <html><head><meta http-equiv="content-type" content="text/html; charset=utf-8"/></head><body>
#            <form action="/sign" method="post">
#            <div><textarea name="content" rows="3" cols="60"></textarea></div>
#            <div><input type="submit" value="please sign"></div>
#            </form>
#            </body></html>""")

class CsvOut(webapp.RequestHandler):
    def get(self):
        threads = {'ScrapingYahoo' : 'http://quote.yahoo.co.jp/'}
        self.response.headers['Content-Type'] = 'text/plain'
        for i in threads :
            SpiderThread( i, threads[ i ] )
        self.redirect('/')

class Guestbook(webapp.RequestHandler):

    def post(self):
        greeting = Greeting()
        if users.get_current_user() :
            greeting.author = users.get_current_user()
        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/')
#        self.response.out.write('<html><body>You wrote:</pre>')
#        self.response.out.write(cgi.escape(self.request.get('content')))
#        self.response.out.write('</pre></body></html>')

class Greeting(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

def main():
    application = webapp.WSGIApplication([
        ('/', MainPage),
        ('/sign', Guestbook),
        ('/csv', CsvOut)
        ],debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
