#!/usr/bin/python
# -*- coding: utf-8 -*-

import gmpy
from Crypto.Util.number import *
import base64

p = 104926859518589

n = 83107041701747003548951619916073267657052136454079830436578267127977699952641

e = 65537

p = pow(p,e,n)
 
y = hex(p).strip('0x').strip('L')
y = y if len(y)%2 == 0 else '0' + y
y = y.decode('hex')

open('custom3.enc','w').write(y)
#print p

