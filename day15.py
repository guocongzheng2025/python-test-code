print("hello")
print("我在学python")
name="郭从政"
age=22
print(name)
print(age)
products=["接口自动化课程", "性能测试训练营", "AI测试资料包"]
print(products)
print(products[0])
print(products[1])
print(products[2])
order={"id": "NO14800", "amount": 199, "status": "paid"}
print(order)
print(order["id"])
print(order["amount"])
print(order["status"])
status="paid"
if status != "paid":
    print("订单已支付")
else:
    print("订单未支付")
for p in products:
    print(p)
for key in order:
    print(key,order[key])
for i in range(3):
    print("第",i,"次测试")
for i in range(1,4):
    print("第",i,"次测试")
for i in range(5):
    print("第",i+1,"次测试")
orders=[{"id": "NO1", "amount": 199}, {"id": "NO2", "amount": 99}]
for o in orders:
    print(o["id"])
username="tester"
print("您好，"+username+"，欢迎登录！")
print(f"您好，{username}，欢迎登录！")
x={"mz":1,"jg":100,"kc":3}
print(f"商品{x['mz']}价格是{x['jg']}元库存{x['kc']}件")
for a in range(1,4):
    print(f"正在测试订单NO{a}")
    print("正在测试订单NO" + str(a))
jiage=200
if jiage < 100:
    print("便宜")
else:
    print("贵")