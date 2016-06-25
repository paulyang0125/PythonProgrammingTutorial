# coding=UTF-8
#!/usr/bin/env
############################################
# WebServer.py
# Author: Paul Yang
# Date: June, 2016
# Brief: the http backend to demostrate tutorial codes 
############################################

import os
from flask import Flask,render_template, request,json,redirect, url_for
from flask import make_response
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER_WINDOWS = '/home/pi/downloaded'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_WINDOWS


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']  
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded successfully'

    
@app.route('/python_demo/<path:path>')
def static_proxy(path):
  print("path:", path)
  #return app.send_static_file(path.encode('utf-8')) #python2.7 require encode otherwise fails with UnicodeError
  return app.send_static_file(path)

@app.route('/demo_submit_form_1', methods=['GET', 'POST'])
def submitForm():
    if request.method == 'POST':
        first_name =  request.form['firstname'];
        last_name = request.form['lastname'];
        return render_template('demo_submit_form_1_result.html', firstname=first_name,lastname=last_name)
    else:
        first_name = request.args.get('firstname')
        last_name = request.args.get('lastname')
        return render_template('demo_submit_form_1_result.html', firstname=first_name,lastname=last_name)
        
@app.route('/')
def hello():
    return 'Welcome to Python Flask!'


if __name__ == "__main__":
    app.run(debug=True)


