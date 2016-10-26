#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	#substitution cipher
	key = 'CRYPTO'
	with open('message.txt','r')as myfile:
		flag=myfile.read()
	print encryptMessage(key,flag)


def encryptMessage(key,message):
	translated = []
	keyIndex=0
	for i in message:
		y=ord(i)^ord(key[keyIndex%6])
		keyIndex+=1
		translated+=chr(y)

	return ''.join(translated).encode('hex')


	#return translated.encode('hex')

if __name__ == '__main__':
	main()