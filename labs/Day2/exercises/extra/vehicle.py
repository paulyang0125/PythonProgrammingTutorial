#!/usr/bin/env
############################################
# vehicle.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################


class Vehicle:
    def __init__(self, name):    
        self.name = name
 
    def move(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")


        
        
class Sportscar(Vehicle):
    def move(self):
        return 'Sportscar driving!'
 
    def stop(self):
        return 'Sportscar breaking!'
        
    def turbo_move(self):
        return 'speed-up x 3'
        
        
class Compactcar(Sportscar):

    def move(self):
        return 'Compactcar driving!'
 
    def stop(self):
        return 'Compactcar breaking!'
 
class (Vehicle):
    def move(self):
        return 'Truck driving slowly because heavily loaded.'
 
    def stop(self):
        return 'Truck breaking!'
 
def drive(CarType):
    return CarType.move()



