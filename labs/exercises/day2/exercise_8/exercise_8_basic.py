#!/usr/bin/env
############################################
# exercise_8_basic.py
# Author: Paul Yang
# Date: June, 2016
# Brief: handling valueError exception 
############################################



############################################
# print_file()
# open file by the filepath user input
# inputs: None
# returns: None
def print_file():
    #data = open("dialogue_chinese.txt", encoding="utf-8")
    filename = input("輸入要開啟的檔名:")
    data = open(filename, encoding="utf-8")
    for line in data:
        try:
            (role,line_spoken) = line.split(":",maxsplit=1)
            print(role,end="")
            print("說: ", end="")
            print(line_spoken, end="")
        except:
            pass
    data.close()