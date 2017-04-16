# Hello world!
# This is a simple python program to help you automatically attach a ".png" extention to a bunch of image files

import os
import string
import shutil

# Here you can specify the file path
path = "C:\Users\Xiaoyan\Google Drive\Images"

i = 0
for filename in os.listdir(path):
	if len(filename.split('.')) == 2:
		continue
	i += 1
	# Here you will get a bunch of strings, i.e. type(filename) = <type 'str'>
	# Then you can customize what you want to do by changing the following code
	# For example, if you have lots of files that have no extensions, replace the
	#  "filename.split('.')[0]" with "filename", which was helping me a lot
	shutil.move(path + "\\" + filename, path + "\\" + filename.split('.')[0] + ".png")

print "Congrats! {} file(s) manipulated done! Go check it out and have a great day!".format(str(i))