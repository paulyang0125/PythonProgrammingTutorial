#!/usr/bin/env
############################################
# extra_power.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################
#def iseven(number):return number % 2 == 0
def file_reading(file_path):
    with open('power.txt', 'r',encoding="utf-8") as nump:
        return nump.read()

nums = list(filter(lambda x: x % 2 == 0,map(int, file_reading('power.txt').split(','))))
power = len(nums) * list(map(int,input("請輸入計算的次方, 例如2代表平方,3次方..."))) 
for i in map(lambda x,p: x**p,nums,power):print(i)



