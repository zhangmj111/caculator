import pytest
import yaml

from src.caculator import Caculator


class TestCaculator:
    @pytest.mark.run(order=1)
    def test_add(self,get_calc,get_data):
        try:
            result = get_calc.add(get_data["add"][0],get_data["add"][1])
            if isinstance(result,float):
                result = round(result,8)
        except Exception as e:
            result = "请输入数字"
        assert result == get_data["add"][2]

    @pytest.mark.run(order=4)
    def test_divide(self,get_calc,get_data):
        try:
            result = get_calc.divide(get_data["divide"][0],get_data["divide"][1])
            if isinstance(result,float):
                result = round(result,8)
        except ZeroDivisionError:
            result = "除数不能为0"
        except Exception as e:
            result = "请输入数字"
        assert result == get_data["divide"][2]

    @pytest.mark.run(order=2)
    def test_minus(self,get_calc,get_data):
        try:
            result = get_calc.minus(get_data["minus"][0],get_data["minus"][1])
            if isinstance(result,float):
                result = round(result,8)
        except Exception as e:
            result = "请输入数字"
        assert result == get_data["minus"][2]

    @pytest.mark.run(order=3)
    def test_multi(self,get_calc,get_data):
        try:
            result = get_calc.multi(get_data["multi"][0],get_data["multi"][1])
            if isinstance(result,float):
                result = round(result,8)
        except Exception as e:
            result = "请输入数字"
        assert result == get_data["multi"][2]


