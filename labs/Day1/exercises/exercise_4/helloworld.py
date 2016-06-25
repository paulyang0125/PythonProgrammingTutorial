# coding=UTF-8
#!/usr/bin/env
############################################
# helloworld.py
# Author: Paul Yang
# Date: June, 2016
# Brief: demo
############################################


filename = input('FileName：')
f = open(filename, 'r', encoding = 'utf8')
b_str = f.read()
f.close()
print(b_str)
