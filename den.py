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
def encode(fileName, password ):
	index = 0
	keys = getShiftKeys( password )
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
def decode(fileName, password ):
	index = 0
	keys = getShiftKeys( password )
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
parser = argparse.ArgumentParser(description='Encode or decode a given text file.  Encodes by default')
parser.add_argument('-d', help='have den decode the file', action='store_true')
parser.add_argument('filename', type=str, help='The name of the target file')
parser.add_argument('password', help='The password used for encoding/decoding')
parser.add_argument('-o', '--output', type=str, help='Name of the output file')
args = parser.parse_args()

inFile = open(args.filename, 'r')
if args.o != None:
	print args.o
	outFile = open(args.o, 'w')
else:
	outFile = open(args.filename + (".decoded" if args.d else ".encoded"), "w")

if args.d:
	print "Decoding: %s" % args.filename
	decode(args.filename, args.password)
else:
	print "Encoding: %s" % args.filename 
	encode(args.filename, args.password)
print "Done"
#--------------------------------------------
#    OOOOOOO
#   O\O   O O
#  O\\\O O   O
#  OOOOOOOOOOO
#  O   O O\\\O
#   O O   O\O
#    OOOOOOO
