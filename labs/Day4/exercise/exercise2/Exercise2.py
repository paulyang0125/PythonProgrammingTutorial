#!/usr/bin/env
############################################
# Exercise2.py
# Author: Paul Yang
# Date: June, 2016
# Brief: 
############################################

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker #like cursor
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu_orm.db')

Base.metadata.bind = engine #make connection between class and actual table
DBSession = sessionmaker(bind = engine) #sqlalchemy execute database operation via vm interface called session 
# a seesion allows us to write down all the command to execute, but it works until we commit
session = DBSession() #session is actual a stage zone for all of the object loaded into db


#Run addmoremenus_second_version.py to populate more menu item 




### Retrieve what "Urban Burger" and 'Super Stir Fry'
print('Retrieve what "Urban Burger" and Super Stir Fry')

tagret_restaurants = session.query(Restaurant).filter(Restaurant.name.in_(['Urban Burger','Super Stir Fry']))
for res in tagret_restaurants:
    print("Restaurant: ",res.name)
    tagret_restaurant_menuitems = session.query(MenuItem).filter(MenuItem.restaurant == res).all()
    for menu in tagret_restaurant_menuitems:
            print("     menuitem: %s price: %s"%(menu.name, menu.price))


print("Retrieve the offer from non-english restaurants")
def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

all_restaurants = session.query(Restaurant)#here 's the query objects, not the list
non_english_restaurants = [res for res in all_restaurants if not isEnglish(res.name)]
for res in non_english_restaurants:
    print("Restaurant: ",res.name)
    non_english_restaurants_menuitems = session.query(MenuItem).filter(MenuItem.restaurant == res).all()
    for menu in non_english_restaurants_menuitems:
        print("     menuitem:", menu.name)

print("Retrieve the restaurants offering 'French Fries' with price smaller than 3 and their description and price")
### Retrieve the restaurants offering 'French Fries' with price smaller than 3 and their description and price 
target_menuitems = session.query(MenuItem).filter(MenuItem.name == "French Fries").filter(MenuItem.price < 3)
for item in target_menuitems:
    print("Restaurant: ",item.restaurant.name)
    print("%s and price: %s" % (item.name, item.price) )