import pytest

from tools import add

data_list=[(0,10,10),(1,6,7),(9,7,16),(1,5,6)]


class TestAdd:
    @pytest.mark.parametrize("a,b,expect", data_list)
    def test_add_1(self,a,b,expect):
        print(f'{a},{b},{expect}')
        assert expect == add(a,b)



