

#!/usr/bin/env
############################################
# countdown.py
# Author: Paul Yang
# Date: June, 2016
# Brief:
############################################

def countdown(n):
    print("counting down from", n)
    while n >0:
        yield n
        n-=1
        
countdown(4)
c = countdown(4)
next(c)
next(c)
next(c)