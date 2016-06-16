#!/usr/bin/env
############################################
# exercise_12.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################

############################################
#  time_each([])
# time each element in the list 
# inputs: a list that contains number only  
# returns: sum 
def time_each(mylist):
    result = 1
    for element in mylist:
		result *= element
    return result       

result = time_each([1,2,3,4])
print(result)


############################################
#  time_each([]) - Recursive version
# time each element in the list 
# inputs: a list that contains number only  
# returns: sum 
def time_each(mylist):
    if len(mylist) == 1:
        return mylist[0]
    else:
        return mylist[0] * time_each(mylist[1:])
        
result = time_each([1,2,3,4])
print(result)


#answer - by reduce and lambda
reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
