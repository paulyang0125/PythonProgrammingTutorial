#!/usr/bin/env
############################################
# parent_3.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################



class Parent(object):
    def altered(self):
        print "PARENT altered()"
class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
dad = Parent()
son = Child()
dad.altered()
son.altered()

