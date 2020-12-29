import os
import pytest
import yaml

from src.caculator import Caculator
path = os.path.split(os.path.realpath(__file__))
with open("./testcaculator.yml",encoding='utf-8') as f:
    data = yaml.safe_load(f)
    print(data)

@pytest.fixture(scope="module")
def get_calc(request):
    print("【开始计算】")
    cal = Caculator()
    yield cal
    print("【计算结束】")

@pytest.fixture(params=data)
def get_data(request):
    data = request.param
    yield data