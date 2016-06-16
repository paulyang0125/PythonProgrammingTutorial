#!/usr/bin/env
############################################
# file_to_file_copy
# Author: Paul Yang
# Date: June, 2016
# Brief: demo argv usage and function
############################################


from sys import argv
from os.path import exists

############################################
# copy_from_to(from, to)
# python file_to_file_copy.py mytest.txt new_file.txt
# inputs: filename of a text file you want to clone
# returns: None
def copy_from_to(from_filename, to_filename):
	input_file = open(from_filename)
	input_data = input_file.read()
	print("The input file is %d bytes long" % len(input_data))
	print("Does the output file exist? %r" % exists(to_filename))
	print("Ready, hit RETURN to continue, CTRL-C to abort.")
	input()
	#raw_input() #used in py2.7 
	output_file = open(to_filename, 'w')
	output_file.write(input_data)
	print("All done!")
	output_file.close()
	input_file.close()

script, from_filename, to_filename = argv
print("Copying from %s to %s" % (from_filename, to_filename))
copy_from_to(from_filename, to_filename)
