# Welcome to den
# The encoder/decoder
import sys
import argparse
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
parser = argparse.ArgumentParser(description='Encode or decode a given text file')
parser.add_argument('<file name>', type=str, help='The name of the target file')
parser.add_argument('e/d', type=chr, help='choose either e for encoding, or d for decodeing')
args = parser.parse_args()

if len(sys.argv) != 2:
	print "Usage: %s filename" % sys.argv[0]
	exit
fileName = sys.argv[1]

inFile = open(fileName, "r")
encode( "01234" )
inFile.close
inFile = open(fileName + ".encoded", "r")
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
