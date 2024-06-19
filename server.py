# server.py

from http.server import HTTPServer, SimpleHTTPRequestHandler
import subprocess

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

def run(server_class=HTTPServer, handler_class=CORSRequestHandler):
    server_address = ('', 8000)  # Serve on port 8000
    httpd = server_class(server_address, handler_class)
    print(f"Starting server at http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
