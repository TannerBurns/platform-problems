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
	key = key.upper()
	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num != -1:
			num += LETTERS.find(key[keyIndex])

			num %= len(LETTERS)

			if symbol.isupper():
				translated.append(LETTERS[num])
			elif symbol.islower():
				translated.append(LETTERS[num].lower())

			keyIndex +=1
			if keyIndex == len(key):
				keyIndex = 0
		else:
			translated.append(symbol)

	return ''.join(translated).encode('hex')


	return translated.encode('hex')

if __name__ == '__main__':
	main()