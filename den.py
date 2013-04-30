# Welcome to den
# The encoder/decoder

# Function Defs
#---------------------------------
# get Shift Keys
def getShiftKeys( password ):
	retval = []
	for ch in password:
		retval += [ord(ch)]
	return retval

# character shift
def charShift( ch, shift):
	retval = ord(ch)
	retval += shift
	if (retval >= 128 ):
		retval = retval%128
	if (retval < 0):
		retval += 128
	return str(unichr(retval))

# encode function
def encode( password ):
	index = 0
	keys = getShiftKeys( password )
	outFile = open("test.txt.encoded", "w")
	for line in inFile:
		text = ""
		for c in line.rstrip("\n"):
			shift = keys[index]
			index = (index+1)%len(keys)
			text += charShift( c, shift )
		outFile.write(text + "\n")
	outFile.close
	return

# decode function
def decode( password ):
	index = 0
	keys = getShiftKeys( password )
	outFile = open("test.txt.decoded", "w")
	for line in inFile:
		text = ""
		for c in line.rstrip("\n"):
			shift = keys[index]
			index = (index+1)%len(keys)
			text += charShift( c, -(shift) )
		outFile.write(text + "\n")
	outFile.close
	return
#--------------------------------------------
# Main
inFile = open("test.txt", "r")
encode( "01234" )
inFile.close
inFile = open("test.txt.encoded", "r")
decode( "01234" )
inFile.close

#--------------------------------------------
#    OOOOOOO
#   O\O   O O
#  O\\\O O   O
#  OOOOOOOOOOO
#  O   O O\\\O
#   O O   O\O
#    OOOOOOO
