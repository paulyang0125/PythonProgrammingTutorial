#!/usr/bin/env
############################################
# exercise_7_2.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################


data = open("dialogue_chinese.txt", encoding="utf-8")
for line in data:
    try:
        (role,line_spoken) = line.split(":",maxsplit=1)
        print(role,end="")
        print("說: ", end="")
        print(line_spoken, end="")
    except:
        pass
data.close()
