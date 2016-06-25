#!/usr/bin/env
############################################
# extra_re.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################



import re
book = open('phone_book.txt','r',encoding = "utf-8")
for line in book:
     if re.search(r"J.*Newhall",line):print(line)
     if re.search('王.婷',line):print(line)
book.close()