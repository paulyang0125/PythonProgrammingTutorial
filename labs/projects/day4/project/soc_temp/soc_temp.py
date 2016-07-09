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


import datetime
import os
import sys
from sys import argv
import time
import sqlite3
from subprocess import call
import re
import subprocess


#DB_NAME = '/home/pi/share/officialProj/' + 'my_db.sqlite'
DB_NAME = os.getcwd() + '/' + 'my_db.sqlite'
FILEPATH = os.getcwd() + '/' + 'temp.log'
CAPTURE_TIME = 5
CAPTURE_TIME_INTERVAL = 2

	
def write_to_file(results):
	
	#remove file if exists as it's for once-time
	if os.path.exists(FILEPATH):
		os.remove(FILEPATH)
	try:
		fp = open(FILEPATH,'w')
		# results are like [apturedUnixTimestamp, timeString, temp]
		results = [r[1] + "  " + r[2] + '\n' for r in results]
		fp.writelines(results)
		
	except IOError:
		print("Error: can\'t find file or write data")
		return False
	
	else:
		print("Written content in the file successfully")
		fp.close()
		return True
		
def write_to_database(results):
	db = sqlite3.connect(DB_NAME)
	cursor = db.cursor()
	for item in results:
		capturedUnixTimestamp = item[0]
		temp = float(item[2])
		cursor.execute('''INSERT INTO soc_temp(date,temp)VALUES(?,?)''',(capturedUnixTimestamp, temp))
	print('Committing transaction for WriteData')
	db.commit()
	db.close()
	return True
    

def capture_temp():
	results= []
	for i in range(CAPTURE_TIME):
		# get timestamp
		dtime = datetime.datetime.now()
		capturedUnixTimestamp = time.mktime(dtime.timetuple()) #convert to UNIX time
		timeString = dtime.strftime("%Y-%m-%d %H:%M:%S")
		# get temp from /opt/vc/bin/vcgencmd measure_temp
		temp = subprocess.check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True)
		# parse temp from check_output
		temp = temp.decode().split("=")[1][:4] # or float(re.findall(r'\d\d.\d', temp.decode()))		
		results.append((capturedUnixTimestamp, timeString, temp))
		print("%d captured, %s , sleep at %d seconds"% (i,temp, CAPTURE_TIME_INTERVAL), end="\n\n")
		time.sleep(CAPTURE_TIME_INTERVAL)
		if not write_to_file(results) or not write_to_database(results):
			return -1
		
	return results
		
		
def main():
	print('start the soc_temp')
	capture_temp()


if __name__ == '__main__':
	sys.exit(main())
		
