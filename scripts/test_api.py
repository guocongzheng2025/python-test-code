# -*- coding: utf-8 -*-
import requests
import pytest
import allure
from common.request_util import BASE, USERNAME, PASSWORD, login
from common.log_util import get_logger
from common.read_data import load_excel_data

logger = get_logger()


@pytest.fixture
def login_token():
    # 登录，把token交给要用的人
    return login()


class TestLoginApi:
    """登录接口真用例"""

    @allure.title("登录接口-正确账号密码返回200")
    def test_login_ok(self):
        resp = requests.post(BASE + "/login", json={"username": USERNAME, "password": PASSWORD})
        data = resp.json()
        assert resp.status_code == 200
        assert data["code"] == 0
        assert data["token"] != ""

    @allure.title("登录接口-数据驱动(Excel:账号/密码/期望)")
    @pytest.mark.parametrize("username,password,expect",
                             [tuple(d.values()) for d in load_excel_data("test_api_login.xlsx")])
    def test_login_driven(self, username, password, expect):
        # 数据驱动：数据在JSON里，expect决定断言方向
        resp = requests.post(BASE + "/login", json={"username": username, "password": password})
        data = resp.json()
        if expect == "ok":
            assert resp.status_code == 200
            assert data["code"] == 0
        else:
            assert resp.status_code == 401
            assert data["code"] == 401


class TestProductApi:
    """商品接口用例"""

    @allure.title("商品接口-带token查询成功")
    def test_products_with_token(self, login_token):
        # 带token查商品
        headers = {"Authorization": "Bearer " + login_token}
        resp = requests.get(BASE + "/products", headers=headers)
        data = resp.json()
        assert data["code"] == 0
        assert len(data["products"]) > 0

    @allure.title("商品接口-不带token返回401")
    def test_products_no_token(self):
        # 不带token查商品 → 401
        resp = requests.get(BASE + "/products")
        assert resp.status_code == 401

    @allure.title("商品接口-存在id=101商品")
    def test_products_has_101(self, login_token):
        # 带token查商品，找id=101
        headers = {"Authorization": "Bearer " + login_token}
        resp = requests.get(BASE + "/products", headers=headers)
        data = resp.json()
        found = False
        for p in data["products"]:
            if p["id"] == 101:
                found = True
        assert found


class TestCartApi:
    """购物车接口用例"""

    @allure.title("购物车接口-带token加购成功")
    def test_cart_add_ok(self, login_token):
        # 带token加购 → 成功
        headers = {"Authorization": "Bearer " + login_token}
        resp = requests.post(BASE + "/cart", json={"productId": 101, "quantity": 1}, headers=headers)
        data = resp.json()
        assert data["code"] == 0

    @allure.title("购物车接口-不带token返回401")
    def test_cart_add_no_token(self):
        # 不带token加购 → 401
        resp = requests.post(BASE + "/cart", json={"productId": 102, "quantity": 1})
        assert resp.status_code == 401


class TestOrderApi:
    """订单接口用例"""

    @allure.title("订单接口-不带token返回401")
    def test_order_no_token(self):
        # 不带token下单 → 401
        resp = requests.post(BASE + "/orders", json={"productId": 101, "quantity": 1})
        assert resp.status_code == 401

    @allure.title("订单接口-下单成功(自给自足)")
    def test_order_create_ok(self, login_token):
        # 自给自足：①清空购物车残留 → ②加购有货商品 → ③下单成功
        headers = {"Authorization": "Bearer " + login_token}
        cart = requests.get(BASE + "/cart", headers=headers).json()
        for item in cart["items"]:                               # 清掉所有残留商品
            requests.delete(BASE + "/cart/" + str(item["productId"]), headers=headers)
        requests.post(BASE + "/cart", json={"productId": 101, "quantity": 1}, headers=headers)  # 加购101(有库存)
        resp = requests.post(BASE + "/orders", json={"productId": 101, "quantity": 1}, headers=headers)
        data = resp.json()
        assert data["code"] == 0
        assert data["order"]["id"] != ""
