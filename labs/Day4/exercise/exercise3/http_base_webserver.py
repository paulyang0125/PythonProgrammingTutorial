#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env
############################################
# http_base_webserver.py
# Author: Paul Yang
# Date: June, 2016
# Brief:
############################################


from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import cgi
debug = False
class WebServerHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        #rootdir = "C:\\Users\\paulyang\\Desktop\\開發中商業\\Teaching\\Python_Teachings\\InProcessing\\making_materials\\Pratices\\day4\\2.HTTPServer\\"
        #rootdir = "day4/exercise/exercise3/"
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            message = b""
            message += bytes("<html><body>Hello, my first http server</body></html>","utf-8")
            self.wfile.write(message)
            print(message)
            return
        elif self.path.endswith("/konnichiwa"):
            f = open(rootdir + "html_jp.html",encoding = 'utf8') #open requested file
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f.read(),'utf-8'))
            f.close()
            return
        elif self.path.endswith("/nihao"):
            f = open(rootdir + "html_tw.html",encoding = 'utf8') #open requested file
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f.read(),'utf-8'))
            f.close()
            return
            

        else:
            self.send_error(404,"File Not Found: %s"%self.path)
            
    

def main():

    try:
        port = 8080
        hostName = ""
        server = HTTPServer((hostName,port),WebServerHandler)
        print(time.asctime(), "Server Starts - %s:%s" % (hostName, port))
        server.serve_forever()
        
    except KeyboardInterrupt:
        print("cont-c entered, stopping web server...")
        server.socket.close()

    
    
if __name__ == '__main__':
    main()
