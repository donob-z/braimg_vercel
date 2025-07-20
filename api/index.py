# -*- coding: UTF-8 -*-
import requests
from http.server import BaseHTTPRequestHandler
import json
from os import environ

GIT_REPO = environ.get("GIT_REPO")
GIT_USER = environ.get("GIT_USER")
GIT_TOKEN = environ.get("GIT_TOKEN")

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if "?" in path:
            img_name = path.split('?')[1]
            data = {
                "url": "https://api.github.com/repos/{user}/{repo}/contents/{img_name}".format(user=GIT_USER, repo=GIT_REPO, img_name=img_name)
            }
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello braimg!".encode('utf-8'))
        
        return
