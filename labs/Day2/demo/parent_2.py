#!/usr/bin/env
############################################
# parent_2.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################

class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "CHILD override()"
dad = Parent()
son = Child()
dad.override()
son.override()


