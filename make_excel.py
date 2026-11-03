# -*- coding: utf-8 -*-
# 生成 test_api_login.xlsx（和 JSON 一样的数据，只是格式变成 Excel）
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(["username", "password", "expect"])
ws.append(["tester", "123456", "ok"])
ws.append(["tester", "wrong", "fail"])
ws.append(["nobody", "123456", "fail"])
wb.save(r"E:\PythonTestCode\data\test_api_login.xlsx")
print("生成成功: data/test_api_login.xlsx")
