# -*- coding: UTF-8 -*-

from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if "?" in path:
            img_name = path.split('?')[1]
            data = {
                "img_name": img_name
            }
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'text')
            self.end_headers()
            self.wfile.write("Hello braimg!".encode('utf-8'))
        
        return
