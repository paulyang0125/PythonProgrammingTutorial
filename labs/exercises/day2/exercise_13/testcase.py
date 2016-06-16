#!/usr/bin/env
############################################
# testcase.py
# Author: Paul Yang
# Date: June, 2016
# Brief: test employee.py
############################################


def test_case():
	paul = Employee('Paul',15000,"teacher")
	jack = Employee('Jack',20000,"manager")
	joy = Employee('Joy',15000,"writter")
	mike = Employee('mike',20000,"teacher")
	#add grade
	paul.add_grade(100)
	paul.add_grade(80)
	paul.add_grade(90)
	print("%s average grade:%d" % (paul.get_name(), paul.display_avg_grade()))
	#add failure grade
	paul.add_grade(40)
	paul.add_grade(30)
	paul.add_grade(58)
	
	print("%s failed clount:%d" % (paul.get_name(), paul.display_failure_count()))
	#add failure grade
	Employee.display_employee_count()
	Employee.display_position_count("manager")
	Employee.display_position_count("teacher")
	Employee.display_position_count("other")
	