###Tanner Burns Soltuion A###
import base64									#don't foget
with open ("given-encoded.txt", "r") as file1:
	lines=file1.readlines()

#with open("output.txt,"w") as file2:			#STEP 1
#	for i in lines:								#for generating output file with  
#		file2.write(base64.b64decode(i)			#readable text

listoftext=[]									#
for i in lines:									# list contains decoded text
	listoftext.append(base64.b64decode(i))		# 

caps=""											#STEP 2
for i in listoftext:							#
	j=0											#this is the logic for extrating
	while j < len(i):							#only capital letters from the	
		if i[j].isupper():						#entire list	
			caps+=i[j]							#	
		j+=1									#

print caps

count=0											#STEP 3
flag=""											#
for i in listoftext:							#this is the logic used to extract the	
	if ((count+1)%8)==0:						#flag from the file
		flag+=i[4:8]							#
	count+=1									#

print flag

