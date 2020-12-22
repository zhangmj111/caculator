import pytest
import yaml

from src.caculator import Caculator

with open("./testcaculator.yml") as f:
    data = yaml.safe_load(f)
class TestCaculator:
    def setup(self):
        self.cal = Caculator()

    @pytest.mark.parametrize("a,b,expect",data["add"])
    def test_add(self,a,b,expect):
        assert self.cal.add(a,b) == expect

    @pytest.mark.parametrize("a,b,expect", data["minus"])
    def test_minus(self,a,b,expect):
        assert self.cal.minus(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", data["multi"])
    def test_multi(self,a,b,expect):
        assert self.cal.multi(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", data["divide"])
    def test_divide(self,a,b,expect):
        assert self.cal.divide(a, b) == expect
