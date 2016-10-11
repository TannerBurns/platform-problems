###Tanner Burns base64 Decoder###
import base64										
with open ("given-easy.txt", "r") as file1:
	lines=file1.readlines()
with open ("output.txt", "w") as file2:
	for i in lines:									
		file2.write(base64.b64decode(i))