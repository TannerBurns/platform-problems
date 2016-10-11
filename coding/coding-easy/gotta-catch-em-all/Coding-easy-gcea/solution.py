###Tanner Burns Soltuion###
import base64						#
with open ("given-easy.txt", "r") as file1:
	lines=file1.readlines()
#with open("output.txt,"w") as file2:				# for generating output file with 
#	for i in lines:									# readable text
#		file2.write(base64.b64decode(i)				#

listoftext=[]										#
for i in lines:										# list contains decoded text
	listoftext.append(base64.b64decode(i))			# 

count=0												#
flag=""												#this is the logic used to extract the	
for i in listoftext:								#flag from the file
	if ((count+1)%8)==0:							#
		flag+=i[4:8]								#
	count+=1										#

print flag