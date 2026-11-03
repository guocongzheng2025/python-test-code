import pytest

from tools import login
from common.read_data import build_data1

class TestLogin:
    @pytest.mark.parametrize('username,password,expect', build_data1())
    def test_username_password_ok(self,username,password,expect):
        #判断预期结果和实际结果是否相符
        print(f'username:{username},password:{password},expect:{expect}')
        assert expect == login(username,password)

