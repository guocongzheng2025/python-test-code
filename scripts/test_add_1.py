from tools import add
class TestAdd:
    def test_add_1(self):
        print('0,10,10')
        assert 10 == add(0,10)
    def test_add_2(self):
        print('1,5,6')
        assert 6 == add(1,5)
    def test_add_3(self):
        print('9,7,16')
        assert 16 == add(9,7)