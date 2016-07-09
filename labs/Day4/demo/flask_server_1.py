# coding=UTF-8
#!/usr/bin/env
############################################
# flask_server_1.py
# Author: Paul Yang
# Date: June, 2016
# Brief: the http backend to demostrate tutorial codes 
############################################



from flask import Flask
app = Flask(__name__)



@app.route('/')
@app.route('/hello')
def HelloWorld():

    return "HelloPython"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)