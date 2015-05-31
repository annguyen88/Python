__author__ = "Andrew Nguyen"
__copyright__ = "Copyright 2015"

__version__ = "0.2"

import os
import sys

userInput = sys.argv[1]
if userInput[0] == "-":
 if userInput == "-help":
  print "I will provide help"

 elif userInput == "-rm":
  print "I will just remove: %s." % sys.argv[2]
  os.rmdir(sys.argv[2])

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


