from tools import add
class TestAdd:
    def test_add_1(self):
        print('0,10,10')
        if 10 == add(0,10):
            print('0.10.10 通过')
        else:
            print('0.10.10 不通过')
    def test_add_2(self):
        print('1,5,6')
        if 6 == add(1,5):
            print('1.5.6 通过')
        else:
            print('1.5.6 不通过')
    def test_add_3(self):
        print('9,7,16')
        if 16 == add(9,7):
            print('9,7,16 通过')
        else:
            print('9,7,16 不通过')