#!/usr/bin/env
############################################
# employee.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################


class Employee:
    """這是一個簡單的類別demo"""
    empCount = 0
    managerCount = 0
    teacherCount = 0
    otherCount = 0
    def __init__(self, name, salary, position):
            self.__name = name
            self.__grades = []
            self.__position = position
            self.__failure_count = 0
            if self.position == "manager":
                Employee.managerCount += 1
            elif self.position == "teacher":
                Employee.teacherCount += 1
            else:
                Employee.otherCount += 1
            self.__salary = salary
            Employee.empCount += 1

    def add_grade(self,grade):
        self.__grades.append(grade)

    def get_name(self):
        return self.__name

    def display_avg_grade(self):
        if self.__grades:
            return sum(self.__grades)/len(self.__grades)
        else:
            print("你沒有輸入評量分數!")

    def display_failure_count(self):
            if self.__grades:
                return len([g for g in self.__grades if g < 60])
            else:
                print("你沒有輸入評量分數!")  
    @classmethod
    def display_position_count(cls, position):
            if position == "manager":
                print("Manager數量： %d" % cls.managerCount)
            elif position == "teacher":
                print("Teacher數量： %d" % cls.teacherCount)
            else:
                print("其他職位數量： %d" % cls.otherCount)
    @classmethod
    def display_employee_count(cls):
            print("Total Employee %d" % cls.empCount)

    def displayEmployee(self):
            print("Name : ", self.name, ", Salary: ", self.salary)
