#!/usr/bin/env
############################################
# exercise_11.py
# Author: Paul Yang
# Date: June, 2016
# Brief:   
############################################



wwwlog = open("access-log")
total = 0
for line in wwwlog:
    bytestr = line.rsplit(None,1)[1]
    if bytestr != '-':
        total += int(bytestr)
print("Total",total)
