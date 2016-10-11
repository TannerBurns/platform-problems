#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():
	key = sys.argv[1]
	text = "DJYE{Qsz_Gq_CyQw}"
	print  decryptMessage(key,text)


def decryptMessage(key,message):
	translated = ""
	for i in range(0,len(message)):
		if message[i].isalpha():
			if message[i].isupper():
				char = chr((ord(message[i])-ord('A')+int(key))%26 + ord('A'))
			else:
				char = chr((ord(message[i])-ord('a')+int(key))%26 + ord('a'))
			translated+=char
		else:
			translated+=message[i]
	
	return translated

if __name__ == '__main__':
	main()