import json
import pytest

from common.read_data import build_data
from tools import add







class TestAdd:
    @pytest.mark.parametrize("a,b,expect", build_data())
    def test_add_1(self,a,b,expect):
        print(f'{a},{b},{expect}')
        assert expect == add(a,b)



