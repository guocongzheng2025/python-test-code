import requests
def login():
    url = "http://43.133.227.52/api/login"
    body = {"username": "tester", "password": "123456"}
    resp = requests.post(url, json=body)
    data = resp.json()  # 把JSON转成字典
    token = data["token"]  # 取出token
    print("token是:", token)
    return token  # 把token交给外面


token = login()  # 调用login，拿到token存进变量

url = "http://43.133.227.52/api/products"
headers = {"Authorization": "Bearer " + token}  # 把token放进请求头
resp = requests.get(url, headers=headers)
print("商品列表:", resp.text)

url = "http://43.133.227.52/api/cart"
body = {"productId": 102, "quantity": 1}
resp = requests.post(url, json=body, headers=headers)
print("加购物车:", resp.text)

url = "http://43.133.227.52/api/orders"
body = {"productId": 101, "quantity": 1}
resp = requests.post(url, json=body, headers=headers)
print("下单：", resp.text)