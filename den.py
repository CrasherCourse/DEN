# Welcome to den
# The encoder/decoder

#------------------------------------------
# encode function
def encode( password ):
	outFile = open("test.txt.encoded", "w")
	for line in inFile:
		text = ""
		for c in line.rstrip("\n"):
			text += str(unichr(ord(c) + 5))
		outFile.write(text + "\n")
	outFile.close
	return
# decode function
def decode( password ):
	outFile = open("test.txt.decoded", "w")
	for line in inFile:
		text = ""
		for c in line.rstrip("\n"):
			text += str(unichr((ord(c) - 5)))
		outFile.write(text + "\n")
	outFile.close
	return
#--------------------------------------------
inFile = open("test.txt", "r")
encode(0)
inFile = open("test.txt.encoded", "r")
decode(0)

inFile.close
#--------------------------------------------
#    OOOOOOO
#   O\O   O O
#  O\\\O O   O
#  OOOOOOOOOOO
#  O   O O\\\O
#   O O   O\O
#    OOOOOOO
