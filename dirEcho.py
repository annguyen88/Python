import os
import sys

userInput = sys.argv[1]
if userInput[0] == "-":
 if userInput == "-help":
  print "I will provide help"

 elif userInput == "-rm":
  print "I will just remove the file"

elif os.path.exists(sys.argv[1]):
 print "Diretory exists. Deleting Dir"
 os.rmdir(sys.argv[1])

else:
 print "directory will be created"

if userInput[0] != "-":
 os.mkdir(sys.argv[1])
 print "Directory has been made"
#os.rmdir(sys.argv[1])
#print ("Directory has been removed")


