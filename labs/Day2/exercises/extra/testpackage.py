#!/usr/bin/env
############################################
# testpackage.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################
from mypackage.subpackage1 import element1
from mypackage.subpackage1 import element2   
from mypackage.subpackage2 import element1
from mypackage.subpackage2 import element2  

print("-- subpackage1 --")
#element1.py
element1.print_name() 
element1.print_path()
#element2.py
element2.print_name() 
element2.print_path()

print("-- subpackage2 --")
#element1.py
element1.print_name() 
element1.print_path()
#element2.py
element2.print_name() 
element2.print_path()