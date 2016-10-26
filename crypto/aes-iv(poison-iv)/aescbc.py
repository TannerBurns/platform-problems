
def modify_block_aes_cbc(plaintext, modifiedtext, initial_vector):
	#save the two 16 byte blocks together in a list of tupples
	diff=[]
	#zip works like a cordinate or pair system to create a tupple
	for a, b in zip(plaintext[:16],modifiedtext[:16]):
		#this creates the difference in the two blocks
		diff += [ord(a) ^ ord(b)]

	#save modified first block in answ
	answ=""
	#join the two blocks together in aes format
	for i in range(16):
		answ += ''.join(["%0.2x" % (int(initial_vector[i*2:i*2+2],16) ^ diff[i])])
	return answ

#modies first block aes-cbc	$1=plaintext		$2=modifiedtext		$3=given Initial Vector
print modify_block_aes_cbc('Pass: sup3r31337','Pass: notAs3cre7','19a9d10c3b155b55982a54439cb05dce')