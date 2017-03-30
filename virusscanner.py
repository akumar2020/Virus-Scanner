# Ask the user for a file to scan
userFile = input("What file would you like to scan for a virus?")

# Read from said file
fread = open(userFile, "r+")

# Tell the user if there is a virus in the file
if "virus" in fread:
	print("Well, crap. There is a virus in this file.")
else:
	print("Yaaaaaaaaaaaaaaaaaaaaaaaaaayyyyyy. This file does not contain a virus. You must be so happy.")