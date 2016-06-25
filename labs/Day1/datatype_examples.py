# coding=UTF-8
#!/usr/bin/env
############################################
# datatype_examples.py
# Author: Paul Yang
# Date: June, 2016
# Brief: demo usage of python data type and operators
############################################


#Arithmetic 
a = 21
b = 10 
c = a + b
print("Line 1: value of c is", c)
c = a - b
print("Line 2: value of c is", c)
c = a * b
print("Line 3: value of c is", c)
c = a / b
print("Line 4: value of c is", c)
c = a % b 
print("Line 5: value of c is", c)
a=2
b = 3
c = a**b 
print("Line 5: value of c is", c)
a=10
b=5
c = a//b 
print("Line 5: value of c is", c)



#var Assignment
a = 21
b = 10
c = 0
c = a + b
print("Line 1: value of c is", c)
c += a
print("Line 2: value of c is", c)
c *= a
print("Line 3: value of c is", c)
c /= a
print("Line 4: value of c is", c)
c = 2
c %= a
print("Line 5: value of c is", c)
c **= a
print("Line 6: value of c is", c)
c //= a # floor division or called integrer division  
print("Line 7: value of c is", c)


#bitwise operations
a = 60 		# 60 = 0011 1100
b = 13 		# 13 = 0000 1101
c = 0
c = a & b; 		# 12 = 0000 1100
print("Line 1: value of c is", c)
c = a | b; 		# 61 = 0011 1101
print("Line 2: value of c is", c)
c = a ^ b; 		# 49 = 0011 0001
print("Line 3: value of c is", c)
c = ~a; 		# -61 = 1100 0011
print("Line 4: value of c is", c)
c = a << 2; 	# 240 = 1111 0000
print("Line 5: value of c is", c)
c = a >> 2; 	# 15 = 0000 1111
print("Line 6: value of c is", c)

#Membership operations
mylist = [5, 4, 3, 2, 1 ]
b = 4
if ‘a’ in mylist:
	print("Line 1 - a is available in the given list")
else:
	print("Line 1 - a is not available in the given list")
if b not in mylist:
	print("Line 2 - b is not available in the given list")
else:
	print("Line 2 - b is available in the given list")
if 5 in mylist:
	print ("Line 3 - 5 is available in the given list")
else:
	print ("Line 3 - 5 is not available in the given list")

#Logical operations
a = 10
b = 20
if ( a and b ):
	print("Line 1 - a and b are true")
else:
	print ("Line 1 - Either a is not true or b is not true")


if ( a or b ):
	print("Line 2 - Either a is true or b is true or both are true")
else:
	print ("Line 2 - Neither a is true nor b is true")
if not( a and b ):
	print ("Line 3 - Either a is not true or b is not true")

else:
	print ("Line 3 - a and b are true")

