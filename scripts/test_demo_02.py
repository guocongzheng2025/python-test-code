# 书写测试类，类名以Test开头
import pytest


class TestDemo:
    # 书写测试方法（将来书写用例的真正代码），方法名以test开头
    def test_demo(self):
        print('测试方法1')
    def test_demo2(self):
        print('测试方法666')

if __name__ == '__main__':
    pytest.main(['-s', 'test_add_2.py'])


