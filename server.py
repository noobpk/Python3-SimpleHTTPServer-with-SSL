#!/bin/python3.8
#server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler, HTTPStatus
import socketserver
import ssl

IP = '127.0.0.1'
PORT = 9090

#Start server without ssl
# httpd = socketserver.TCPServer((IP, PORT), SimpleHTTPRequestHandler)

#Start server with ssl
httpd = HTTPServer((IP, PORT), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (
	httpd.socket, server_side=True,
    certfile='/path/to/cert.pem')

print("Server start at: https://{}:{}".format(IP, PORT))
httpd.serve_forever()