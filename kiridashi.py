import os
import sys
import re


f=open('modenaerr.log', 'r')
#p = re.compile('INSERT INTO .*\)\]$')
#p = re.compile('UPDATE TDN_ORDER SET .*$')
p = re.compile('ERR  :SQL : .*$')
for s in f.readlines():
  a = p.search( s )
  if a :
    print a.group()
  else :
    pass

