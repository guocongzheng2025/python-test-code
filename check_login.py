# -*- coding: utf-8 -*-
import requests

url = "http://43.133.227.52/api/login"

# 正确密码
r1 = requests.post(url, json={"username": "tester", "password": "123456"})
print("正确密码 -> HTTP:", r1.status_code, "| body:", r1.text)

# 错误密码
r2 = requests.post(url, json={"username": "tester", "password": "wrong"})
print("错误密码 -> HTTP:", r2.status_code, "| body:", r2.text)

# 错误用户名
r3 = requests.post(url, json={"username": "nobody", "password": "123456"})
print("错误用户 -> HTTP:", r3.status_code, "| body:", r3.text)
