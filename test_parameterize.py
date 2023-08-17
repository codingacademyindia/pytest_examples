import pytest

def calculate_rectangle_area(length, width):
    return length * width

@pytest.mark.parametrize("length, width, expected", [
    (2, 3, 6),     # Test case 1
    (0, 5, 0),     # Test case 2
    (4, 0, 0),     # Test case 3
    (5, 5, 25),    # Test case 4
])
def test_calculate_rectangle_area(length, width, expected):
    result = calculate_rectangle_area(length, width)
    assert result == expected
