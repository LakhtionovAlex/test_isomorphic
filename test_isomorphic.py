import pytest
from main import isomorphic


@pytest.mark.parametrize('str1,str2', [("", ""), (", t = ", ""), ("egg", "add"), ("paper", "title"), ("!!!", "!!!")])
def test_positive_isomorphic(str1: str, str2: str):
    res = isomorphic(str1, str2)
    assert res


@pytest.mark.parametrize('str1,str2', [("foo", "bar"), ("see", "sed"), ("123", "443")])
def test_negative_isomorphic(str1: str, str2: str):
    res = isomorphic(str1, str2)
    assert not res


if __name__ == '__main__':
    print("Complete")
