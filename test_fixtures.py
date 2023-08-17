import pytest

@pytest.fixture
def before_test():
    print("\nbefore test....\n")

@pytest.mark.bvt
def test_uppercase(before_test):
    assert "loud noises".upper() == "LOUD NOISES"

@pytest.mark.bvt
def test_lower_case(before_test_conftest):
    assert "Loud Noises".lower() == "loud noises"

@pytest.mark.regression
def test_capitalized(before_test):
    assert "Loud noises"[0] == "L"


