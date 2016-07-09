# coding=UTF-8
#!/usr/bin/env
############################################
# flask_server_3.py
# Author: Paul Yang
# Date: June, 2016
# Brief: the http backend to demostrate tutorial codes 
############################################

from flask import Flask
app = Flask(__name__)


##2 add CRUD 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu_orm.db')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_Menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += '</br>'
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br>'
        output += '</br>'
    return output


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)