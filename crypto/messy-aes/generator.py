#!/usr/bin/python
# -*- coding: utf-8 -*-

from random_words import RandomWords
from Crypto import Random
from Crypto.Cipher import AES
import base64
import os

BLOCK_SIZE=16
passphrase="\x00"+os.urandom(30)+"\x00"

rw = RandomWords()

word = rw.random_word()

beg="FLAG{"
end="}"

IV = Random.new().read(BLOCK_SIZE)
aes = AES.new(passphrase, AES.MODE_CFB, IV)


for i in range(0,15000):
	word1 = rw.random_word()
	word2 = rw.random_word()
	word3 = rw.random_word()
	word4 = rw.random_word()
	word5 = rw.random_word()
	word6 = rw.random_word()
	message = beg + str(word1) + "_" + str(word2) + "_" + str(word3) + "_" + str(word4) + "_" + str(word5) + "_" + str(word6) + end
	enc = base64.b32encode(aes.encrypt(message))
	enc = enc.replace("=","")
	enc = enc.lower()
	print str(message) + ":" + str(enc)