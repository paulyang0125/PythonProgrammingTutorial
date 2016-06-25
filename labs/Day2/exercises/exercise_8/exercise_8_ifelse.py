#!/usr/bin/env
############################################
# exercise_8_ifelse.py
# Author: Paul Yang
# Date: June, 2016
# Brief: handling the exception of ValueError and FileNotFoundError  
############################################



############################################
# print_file()
# open file by the filepath user input and will check if the filepath is valid  
# inputs: None
# returns: None
import os
def print_file():
    filename = input("輸入要開啟的檔名:")
    if os.path.exists(filename):
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
    else:
        print("檔名不存在")
    