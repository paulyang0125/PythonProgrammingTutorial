#!/usr/bin/env
############################################
# extra_listcomprehension.py
# Author: Paul Yang
# Date: June, 2016
# Brief:   
############################################


#list comprehesion 
[ [1 if i == j else 0 for j in range(0,3)] for i in range(0,3)]



#forloop

list1 = []
for i in range(0,3):
    list2 = []
    for j in range(0,3):
        if j == i:
            list2.append(1)
        else:
            list2.append(0)
    list1.append(list2)  