# -*- coding: utf-8 -*-
import json

from config import BASE_DIR


def build_data():
    with open(BASE_DIR + '/data/add.json', encoding='utf-8') as f:
        data = json.load(f)
    return data


'''if __name__ == '__main__':
    print(build_data())'''


def build_data1():
    with open(BASE_DIR + '/data/login.json', encoding='utf-8') as f:
        data = json.load(f)
    new_list = []
    for d in data:  # d字典，字典中 值是否都需要
        d.pop('desc')
        new_list.append(tuple(d.values()))
    return new_list


def load_json_data(file_name):
    """读取 data/ 下的json文件，返回字典列表（通用版）"""
    with open(BASE_DIR + '/data/' + file_name, encoding='utf-8') as f:
        return json.load(f)


def load_excel_data(file_name):
    """读取 data/ 下的Excel文件，返回字典列表（Excel版数据驱动）"""
    from openpyxl import load_workbook
    wb = load_workbook(BASE_DIR + '/data/' + file_name)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    headers = rows[0]  # 第一行是表头
    return [dict(zip(headers, row)) for row in rows[1:]]


if __name__ == '__main__':
    print(build_data1())
