#!/usr/bin/env
############################################
# exercise_7.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################


data = open("dialogue_chinese.txt", encoding="utf-8")
for line in data:
    if len(line.split(":")) > 2:
        (role,line_spoken,another) = line.split(":")
        print("error: ",role,line_spoken,another)
        continue
    else:
        (role,line_spoken) = line.split(":")

    print(role,end="")
    print("說: ", end="")
    print(line_spoken, end="")