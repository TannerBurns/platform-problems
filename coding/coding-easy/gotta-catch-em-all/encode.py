import base64

with open ("given-decoded.txt", "r") as myfile:
	lines=myfile.readlines()
with open("given-encoded.txt", "w") as file2:
	for i in lines:
		file2.write(base64.b64encode(i) + "\n")

