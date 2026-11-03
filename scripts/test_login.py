from tools import login


class TestLogin:
    def test_username_password_ok(self):
        #判断预期结果和实际结果是否相符
        assert"登录成功" == login("admin","123456")

    def test_username_error(self):
        # 判断预期结果和实际结果是否相符
        assert "登录失败" == login("root", "123456")

    def test_password_error(self):
        # 判断预期结果和实际结果是否相符
        assert "登录失败" == login("admin", "123123")

    def test_username_password_error(self):
        # 判断预期结果和实际结果是否相符
        assert "登录失败" == login("aaa", "123123")