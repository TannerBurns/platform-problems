
##needed string##
#	po6vko2hb574zjwxurkayebnio33mnmuhwhhvtwk2tlqsghnasyb2kfmzu7ckz7lrvcabdsmisereryubq
##first 8bytes
fsb='po6vko2hb574zjwx'
lines=[]
with open('given.txt') as f:
	for line in f:
		if fsb in line:
			print "Found flag:\n"
			print line
