# coding=UTF-8
#!/usr/bin/env python3

##################################################################################
#                                                                                #
#  Copyright (c) 2016 Yao Nien, Yang, paulyang0125@gmail.com                     #  
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not   #
#  use this file except in compliance with the License. You may obtain a copy    #
#  of the License at http://www.apache.org/licenses/LICENSE-2.0. Unless required #
#  by applicable law or agreed to in writing, software distributed under the     #
#  License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS  #
#  OF ANY KIND, either express or implied. See the License for the specific      #
#  language governing permissions and limitations under the License.             # 
#                                                                                #
##################################################################################


from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
app = Flask(__name__)
user_name = "Paul"



#setup for temp capture
import datetime
import os
import time
import sqlite3
from time import sleep
DBPATH = os.getcwd() + '/soc_temp/' + 'my_db.sqlite'
FILEPATH = os.getcwd() + '/soc_temp/' + 'temp.log'

# Initialise the gpio settings
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   22 : {'type': 'output', 'name' : 'led_22', 'state' : GPIO.LOW},
   27 : {'type': 'output', 'name' : 'led_27', 'state' : GPIO.LOW},
   23 : {'type': 'input', 'name' : 'sw_01', 'state' : GPIO.HIGH},
   24 : {'type': 'input', 'name' : 'sw_02', 'state' : GPIO.HIGH}
   }
   
# Set each LED pin as an output and make it low: 
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)

# set SW button as input 
GPIO.setup(23, GPIO.IN) 
GPIO.setup(24, GPIO.IN) 

# Initialise the LCD class
from LCD.mylcd import mylcd
lcd = mylcd()
lcd.LCD_boot_setup()
lcd.clear_line_1()
lcd.move(1,1)


@app.route("/")
def main():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {'user_name' : user_name,'time': timeString}
	return render_template('index_1.html', **templateData)




#### GPIO ####
@app.route("/GPIO")
def GPIO_main():
	# For each pin, read the pin state and store it in the pins dictionary:
	for pin in pins:
		pins[pin]['state'] = GPIO.input(pin)

	# Put the pin dictionary into the template data dictionary:
	templateData = {'pins' : pins}
	# Pass the template data into the template main.html and return it to the user
	return render_template('gpio_main_1.html', **templateData)
   
   
   
   
@app.route("/GPIO/<changePin>/<action>")
def action(changePin, action):
    # Convert the pin from the URL into an integer:
    changePin = int(changePin)
    # Get the device name for the pin being changed:
    deviceName = pins[changePin]['name']

    # If the action part of the URL is "on," execute the code indented below:
    if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
  
    if action == "off":
          GPIO.output(changePin, GPIO.LOW)
          message = "Turned " + deviceName + " off."

    if action == "read":
       if GPIO.input(changePin) == GPIO.HIGH:
	       message = deviceName + " is not pressed."
       else: 
	       message = deviceName + " is pressed."

    # For each pin, read the pin state and store it in the pins dictionary:
    for pin in pins:
	    pins[pin]['state'] = GPIO.input(pin)

    # Along with the pin dictionary, put the message into the template data dictionary:
    templateData = {'message' : message,'pins' : pins}
    return render_template('gpio_main_1.html', **templateData)
	
	

#### SOC_TEMP_LOG ####
   
@app.route("/TEMP")
def TEMP_main():
	return render_template('soc_temp_main_1.html')
   

@app.route("/TEMP/recent")
def get_temp_from_file(): 
	
	temps = list()
	print(" file: %s",FILEPATH )
	if os.path.exists(FILEPATH):
		try:
			fp = open(FILEPATH,'r')
			for line in fp:
				temp = dict()
				temp['date'] = line.split()[0] + ' ' + line.split()[1]
				#temp['time'] = line.split()[1]
				temp['temp'] = line.split()[2]
				print ("DEBUG: " + temp['date'] + " " + temp['temp'])
				temps.append(temp)
		except IOError:
			print("Error: can\'t find file or write data")
			message = "Error: can\'t find file or write data"
			templateData = {'message' : message,'temps' : temps}
			#templateData = jsonify(templateData)
			#templateData.status_code = 200
			return render_template('soc_temp_main.html', data = templateData)
			
		else:
			print("read content in the file successfully")
			message = "read file successfully"
			fp.close()
			templateData = {'message' : message,'temps' : temps}
			return render_template('soc_temp_main_1.html', data = templateData)

	else:
		print("Error: no log file exist\n")
		print("Please retrieve data by pressing get-temp-now button")
		message = "Error: no log file exist\n" + "Please retrieve data by pressing get-temp-now button"
		templateData = {'message' : message,'temps' : temps}

		return render_template('soc_temp_main_1.html', data = templateData)
			  
	
		   


@app.route("/TEMP/timeslot", methods=['POST'])
def get_temp_from_db():
	temps = list()
    #make sql statement to filter data by the timeslot from 10,5,2,1 day before
	sqltest = '''select *  from soc_temp  where strftime('%Y-%m-%d %H:%M:%S', datetime(date, 'unixepoch' , 'localtime'))  >  datetime('now','localtime', '-10 days')'''
	sql1d = '''select *  from soc_temp  where strftime('%Y-%m-%d %H:%M:%S', datetime(date, 'unixepoch' , 'localtime'))  >  datetime('now','localtime', '-1 days')'''
	sql2d = '''select *  from soc_temp  where strftime('%Y-%m-%d %H:%M:%S', datetime(date, 'unixepoch' , 'localtime'))  >  datetime('now','localtime', '-2 days')'''
	sql5d = '''select *  from soc_temp  where strftime('%Y-%m-%d %H:%M:%S', datetime(date, 'unixepoch' , 'localtime'))  >  datetime('now','localtime', '-5 days')'''
	
	
	conn=sqlite3.connect(DBPATH,timeout=1)
	select = request.form.get('timerange')
	print("select: %s" % select)
	if select == "1d":
		cursor = conn.execute(sql1d)
		message = "created 1 day data"


	elif select == "2d":
		cursor = conn.execute(sql2d)
		message = "created 2 days data"

	elif select == "5d":
		cursor = conn.execute(sql5d)
		message = "created 5 days data"
	else:
		cursor = conn.execute(sqltest)
		message = "created test data"
		
	all_rows = cursor.fetchall()
	
	for row in all_rows:
		temp = dict()
		temp['date'] = str(datetime.datetime.fromtimestamp(row[1]).strftime("%Y-%m-%d %H:%M:%S"))
		temp['temp'] = str(row[2])
		print ("DEBUG: " + temp['date'] + " " + temp['temp'])
		temps.append(temp)
	
	templateData = {'message' : message,'temps' : temps}
	conn.close()
	
	return render_template('soc_temp_main_1.html', data = templateData)
	
#### LCD ####

@app.route("/LCM")
def LCM_main():
	return render_template('lcd_main.html')

	
@app.route("/LCM/send", methods=['POST'])
def change():
	if request.method == 'POST':
		# Get the value from the submitted form
		lcdText = request.form['lcd']
		print("---Message is", lcdText)
		lcd.clear_line_1()
		lcd.clear_line_2()
		lcd.move(1,1)
		lcd.write_msg(lcdText)
		sleep(1)
	else:
		lcdText = None
	#return redirect(url_for('LCM_main', value=lcdText))
	return render_template('lcd_main.html', value=lcdText)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
