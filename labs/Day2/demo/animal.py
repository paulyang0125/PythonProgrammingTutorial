#!/usr/bin/env
############################################
# animal.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################



class Animal:
   def __init__(self, name=''):
      self.name = name
   def talk(self):# Abstract method, defined by convention only
      raise NotImplementedError("Subclass must implement abstract method")
class Cat(Animal):
   def talk(self):
      print("Meow!")
class Dog(Animal):
   def talk(self):
      print("Woof!")

c = Cat("Missy")
c.talk()
d = Dog("Rocky")
d.talk()
