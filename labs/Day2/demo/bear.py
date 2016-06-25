
#!/usr/bin/env
############################################
# bear.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################

class Bear(object):
    def sound(self):
        print "Groarrr"
 
class Dog(object):
    def sound(self):
        print "Woof woof!"
 
def makeSound(animalType):
    animalType.sound()
 
bearObj = Bear()
dogObj = Dog()
makeSound(bearObj)
makeSound(dogObj)
