#!/usr/bin/env
############################################
# encapsulation.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################

class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b 
        self.__private = c
        
from encapsulation import Encapsulation
x = Encapsulation(11,13,17)
x.public

x._protected

x._protected = 23
x._protected
x.__private
