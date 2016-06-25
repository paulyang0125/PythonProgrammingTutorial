#!/usr/bin/env
############################################
# age.py
# Author: Paul Yang
# Date: June, 2016
# Brief: demo
############################################


age = int(input('How old are you? ')) 
if age <= 2: 
	print(' free') 
elif 2 < age < 13: 
	print(' child fare')
	if(age == 12):
		print('bango! my age')
else: 
	print('adult fare')
