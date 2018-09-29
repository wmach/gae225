# -*- encoding: utf-8 -*-
import os
import time

wao = {'225'        : 12234.00,
       '225f'       : 12000.00,
       'updatedate' : '2008/10/15 Wed 15:15:00',
       'getdate'    : time.ctime(time.time())
       }
for w in wao :
    if w == 't_no' :
        print ('%s' % wao[w])
    elif w =='nk225' :
        print('%s' % wao[w])
    elif w =='nk225f' :
        print('%s' % wao[w])
    elif w =='updatedate' :
        print('%s' % wao[w])
    elif w =='getdate' :
        print('%s' % wao[w])

