# coding=UTF-8
#!/usr/bin/env
############################################
# http_base_webserver_1.py
# Author: Paul Yang
# Date: June, 2016
# Brief: the http backend to demostrate tutorial codes 
############################################


from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import cgi
debug = False
class WebServerHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            message = b""
            message += bytes("<html><body>Hello, my first http server</body></html>","utf-8")
            self.wfile.write(message)
            print(message)
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
