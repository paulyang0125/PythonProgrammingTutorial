# coding=UTF-8
#!/usr/bin/env
############################################
# flask_server.py
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




@app.route('/')
@app.route('/hello')
def HelloWorld():
    #list first restaurant and its menu items
    target_restaurant = session.query(Restaurant).filter_by(name = "大宅門").first()
    items = session.query(MenuItem).filter_by(restaurant_id = target_restaurant.id)
    output = ''
    output += '<h1>' + target_restaurant.name + '</h1>'
    output += '</br>'
    for item in items:
        output += item.name
        output += '</br>'
        output += str(item.price)
        output += '</br>'
        output += item.description
        output += '</br>'
        output += '</br>'

    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)