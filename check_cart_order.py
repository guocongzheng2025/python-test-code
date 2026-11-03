# -*- coding: utf-8 -*-
import requests

BASE = "http://43.133.227.52/api"

r = requests.post(BASE + "/login", json={"username": "tester", "password": "123456"})
token = r.json()["token"]
headers = {"Authorization": "Bearer " + token}

# 方案A：加购缺货商品103，再下单
ra = requests.post(BASE + "/cart", json={"productId": 103, "quantity": 1}, headers=headers)
print("加购103:", ra.status_code, ra.text[:100])
ro = requests.post(BASE + "/orders", json={"productId": 101, "quantity": 1}, headers=headers)
print("加购103后下单:", ro.status_code, ro.text[:120])

# 方案B：加购有货商品102，再下单（购物车现在有103+102）
rb = requests.post(BASE + "/cart", json={"productId": 102, "quantity": 1}, headers=headers)
print("加购102:", rb.status_code, rb.text[:100])
ro2 = requests.post(BASE + "/orders", json={"productId": 101, "quantity": 1}, headers=headers)
print("加购102后下单:", ro2.status_code, ro2.text[:120])
