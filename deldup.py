import os
import sys
import re

#f=open('gomi.err.sql', 'r')
f=open('sql.err.20081014.txt', 'r')
a = []
for i, s in enumerate(f.readlines()):
  if i == 0 :
    a.append( s )
  for a2 in a[-1:] :
    if a2 == s :
      pass
    else :
      a.append( s )

for ex in a :
    print ex
