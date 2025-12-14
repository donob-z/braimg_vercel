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
            img_name = path.split('?')[1].split('&')[0] 
            git_url = "https://api.github.com/repos/{user}/{repo}/contents/{img_name}".format(user=GIT_USER, repo=GIT_REPO, img_name=img_name)
            headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": "Bearer {git_token}".format(git_token=GIT_TOKEN),
                "X-GitHub-Api-Version": "2022-11-28",
            }
            res = requests.get(url=git_url, headers=headers)
            origin_url = res.json()["download_url"]
            img_res = requests.get(url=origin_url)

            self.send_response(200)
            self.send_header('Content-type', img_res.headers.get('Content-Type', 'image/jpeg'))
            self.send_header('Content-Length', len(img_res.content))
            self.end_headers()
            self.wfile.write(img_res.content)
        else:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello PNG.NG!".encode('utf-8'))
        
        return

