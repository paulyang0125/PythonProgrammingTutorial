#!/usr/bin/env
############################################
# exercise_11_pipeline.py
# Author: Paul Yang
# Date: June, 2016
# Brief:   
############################################



wwwlog = open("access-log")
bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
bytes = (int(x) for x in bytecolumn if x != '-')
print("Total", sum(bytes))

