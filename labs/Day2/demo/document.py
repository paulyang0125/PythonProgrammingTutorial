
''' # perhap pdf, word
for document in documents:
    print document.name + ': ' + document.show()

'''


#!/usr/bin/env
############################################
# document.py
# Author: Paul Yang
# Date: June, 2016
# Brief: this is to show HOWTO of python class, __init__method, accessing instance/class attribute  
############################################

class Document:
    def __init__(self, name):    
        self.name = name
 
    def show(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'
 
class Word(Document):
    def show(self):
        return 'Show word contents!'
 
documents = [Pdf('Document1'),
             Pdf('Document2'),
             Word('Document3')]
 
for document in documents:
    print document.name + ': ' + document.show()