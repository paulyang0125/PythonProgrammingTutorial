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


import sqlite3
import os

DB_NAME = os.getcwd() + '/' + 'my_db.sqlite'

def do_database_work(do_create):
	db = sqlite3.connect(DB_NAME)        
	try:
		cursor = db.cursor()
		if do_create:
			print("table doesn't exist, create table")
			create_tables(cursor)

	except sqlite3.Error as er:
		print('Database error %s happened',er)
		db.rollback()
		print('Rolling back transaction')
		raise
	else:
		print('Committing transaction for table creatation')
		db.commit()
		db.close()

def create_tables(cursor):
	print ('Creating tables')
	SQLScript = '''CREATE table soc_temp( id integer primary key, date timestamp default (strftime('%s', 'now', 'localtime')),temp REAL)'''
	cursor.execute(SQLScript)
	
	
def main():
	do_create = not os.path.exists(DB_NAME)
	do_database_work(do_create)
	
	
if __name__ == '__main__':
	main()