#!/usr/bin/env
############################################
# parent_1.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################



class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()
dad.implicit()
son.implicit()
#PARENT implicit()
#PARENT implicit()
