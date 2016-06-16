#!/usr/bin/env
############################################
# exercise_8_try_except.py
# Author: Paul Yang
# Date: June, 2016
# Brief: handling the exception of ValueError and FileNotFoundError  
############################################



############################################
# print_file()
# open file by the filepath user input and catch ValueError and IOError if 
# the fileformat is not appropriate and file doesn't exist
# inputs: None
# returns: None
def print_file():
    filename = input("輸入要開啟的檔名:")
    try:
        data = open(filename, encoding="utf-8")
        for line in data:
            try:
                (role,line_spoken) = line.split(":",maxsplit=1)
                print(role,end="")
                print("說: ", end="")
                print(line_spoken, end="")
            except ValueError:
                pass
        data.close()
    except IOError as err:
        print("檔名不存在")
        print(err)