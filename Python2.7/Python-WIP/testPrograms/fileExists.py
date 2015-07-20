import os.path
import glob

check2 = glob.glob("hello*")
check = os.path.isfile("hello*")
if check2 == True:
	print("File exists")
else:
	print("File doesn't exists")


print glob.glob('hello*')
print check2
print os.path.isfile("hello") 
