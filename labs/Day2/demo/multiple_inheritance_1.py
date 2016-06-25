#!/usr/bin/env
############################################
# multiple_inheritance_1.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################


class CL1(object):
    def __init__(self):
        super(CL1, self).__init__()
        print("class 1 init “)

class CL2(object):
    def __init__(self):
        super(CL2, self).__init__()
        print("class 2 init“)

class CL3(CL1, CL2):
    def __init__(self):
        super(CL3, self).__init__()
        print("class 3 init“)

instance = CL3()

