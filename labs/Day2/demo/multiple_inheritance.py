#!/usr/bin/env
############################################
# multiple_inheritance.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################


class CL1(object):
    def __init__(self):
        print("class 1 init")
    def print_CL1(self):
        print("class 1")
class CL2(object):
    def __init__(self):
        print "class 2 init"
    def print_CL2(self):
        print("class 2")
class CL3(CL2, CL1):
    pass
instance = CL3()
instance.print_CL1()
instance.print_CL2()

