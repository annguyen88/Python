# Author Andrew Nguyen
# July 20, 2015

import fnmatch
import os


#Good library for finding files

for file in os.listdir('/Users/nguyenan/Desktop'):
    if fnmatch.fnmatch(file, 'html*.zip'):
        print file
