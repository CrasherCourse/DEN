# Welcome to den
# The encoder/decoder

# Function Defs
#-----------------------------
# encode function
def encode( password ):
	index = 0
	keys = [1, 2, 3, 4, 5]
	outFile = open("test.txt.encoded", "w")
	for line in inFile:
		text = ""
		for c in line.rstrip("\n"):
			shift = keys[index]
			index = (index+1)%len(keys)
			text += str(unichr(ord(c) + shift))
		outFile.write(text + "\n")
	outFile.close
	return
# decode function
def decode( password ):
	index = 0
	keys = [1, 2, 3, 4, 5]
	outFile = open("test.txt.decoded", "w")
	for line in inFile:
		text = ""
		for c in line.rstrip("\n"):
			shift = keys[index]
			index = (index+1)%len(keys)
			text += str(unichr(ord(c) - shift))
		outFile.write(text + "\n")
	outFile.close
	return
#--------------------------------------------
# Main
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
