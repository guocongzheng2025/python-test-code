# -*- coding: utf-8 -*-
import requests

url = "http://43.133.227.52/api/login"
body = {"username": "tester", "password": "123456"}

resp = requests.post(url, json=body)
print("状态码:", resp.status_code)
print("返回:", resp.text)
