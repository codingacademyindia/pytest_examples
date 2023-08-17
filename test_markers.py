import pytest


@pytest.mark.bvt
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

@pytest.mark.bvt
def test_lower_case():
    assert "Loud Noises".lower() == "loud noises"

@pytest.mark.regression
def test_capitalized():
    assert "Loud noises"[0] == "L"


