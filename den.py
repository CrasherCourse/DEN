# Welcome to den
# The encoder/decoder

inFile = open("test.txt", "r")
outFile = open("test.txt.output", "w")
for line in inFile:
	print line.rstrip("\n")				# removes
	text = ""
	for c in line.rstrip("\n"):
		text += str(unichr(ord(c) + 5))
	print text
	outFile.write(text + "\n")
	decoded = ""
	for c in text:
		decoded += str(unichr(ord(c) - 5))
	print decoded

inFile.close
outFile.close
