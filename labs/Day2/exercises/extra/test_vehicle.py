
#!/usr/bin/env
############################################
# test_vehicle.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################

from vehicle import Truck, Sportscar, Compactcar

cars = [Truck('Mitush'),
        Truck('Orangetruck'),
        Sportscar('Z3'),Compactcar('Polo')]
print("--- test abstract methods ---")        
for car in cars:
    print(car.name + ': ' + car.move())
print("--- test common methods with different object ---")         
for car in cars:
    print(car.name + ': ' + drive(car))
print("--- test in inherited methods turbo ---") 
yaris = Compactcar('Yaris') 
yaris.turbo_move()