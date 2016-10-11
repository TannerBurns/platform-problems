#!/usr/bin/python
# -*- coding: utf-8 -*-

from pwn import *

host = '127.0.0.1'
port = 11111
r = remote(host,port)
flags=["Flag","FLAG","flag"]

while True:
	x = r.recv(2048)
	print x
	if any(f in x for f in flags):
		r.close()
		exit()
	y=x.decode('base64')
	print y
	y+='\n'
	r.send(y)

r.close()
