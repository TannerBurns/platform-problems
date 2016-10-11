#!/usr/bin/python
# -*- coding: utf-8 -*-

from pwn import *
import sys

host = '127.0.0.1'
port = 9999
r = remote(host,port)

#first round
d=r.recv(2048)
print d
r.send("S\n")

#second round
d=r.recv(2048)
print d
r.send("e\n")

#third round
d=r.recv(2048)
print d
r.send("c\n")

#fourth round
d=r.recv(2048)
print d
r.send("r\n")

#fifth round
d=r.recv(2048)
print d
r.send("e\n")

#sixth round
d=r.recv(2048)
print d
r.send("t\n")

#flag
d=r.recv(2048)
print d

r.close()
