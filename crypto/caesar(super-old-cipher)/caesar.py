#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	#substitution cipher
	#key = 'CRYPTO'
	#caeser cipher, key = 24
	flag = 'FLAG{CaEsaR_Is_EaSy}'
	checkValidKey(key)
	print encryptMessage(key,flag)

def checkValidKey(key):
	kList=list(key)
	lList=list(LETTERS)
	kList.sort()
	lList.sort()
	if kList != lList:
		sys.exit("There is an error in the key or symbol set.")

def encryptMessage(key,message):
	translated = ""
	charA=LETTERS
	charB=key
	for symbol in message:
		if symbol.upper() in charA:
			symIndex=charA.find(symbol.upper())
			if symbol.isupper():
				translated+= charB[symIndex].upper()
			else:
				translated+= charB[symIndex].lower()
		else:
			translated+=symbol
	return translated

if __name__ == '__main__':
	main()