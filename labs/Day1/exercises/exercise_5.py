#!/usr/bin/env
############################################
# exercise_5.py
# Author: Paul Yang
# Date: June, 2016
# Brief: demo while and forloop for n * n time matrix, such as n=2 print 1x1, 1x2, 2x1, 2x2 
############################################


n = input('輸入n for n x n matrix\n')

#forloop implementation 
for i in range(1,int(n) + 1):
    for j in range(1,int(n)+1):
        print("%d * %d = %d " % (i,j,i*j))

#whileloop implementation 

i = 1
while i < int(n)+1:
    j = 1
    while j < int(n)+1: 
        print("%d * %d = %d " % (i,j,i*j))
        j += 1
    i += 1