# Welcome to den
# The encoder/decoder

inFile = open("none.txt", "r")
outFile = open("none.txt.output", "w")
for line in inFile:
	print line.rstrip("\n")				# removes
	text = ""
	for c in line.rstrip("\n"):
		text += str(unichr(ord(c) + 5))
	print text
	outFile.write(text + "\n")

inFile.close
outFile.close
