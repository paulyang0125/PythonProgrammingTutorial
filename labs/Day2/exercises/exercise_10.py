#!/usr/bin/env
############################################
# exercise_10.py
# Author: Paul Yang
# Date: June, 2016
# Brief:   
############################################


#questiion - Intervene ‘spam’ with ‘SPAM’ 
result = []
for x in 'spam’':
    for y in  'SPAM':
        result.append(x+y)
result

#questiion - Intervene even and odd number
result = []
for x in range(5):
	if x % 2 == 0
		for y in range(5):
			if y % 2 == 1:
				result.append((x,y))		

                

#answers
[x + y for x in 'spam' for y in 'SPAM']
[(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]

