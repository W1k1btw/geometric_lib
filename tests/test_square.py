import pytest
from geometric_lib.square import square_area, square_perimeter

def test_square_area():
    assert square_area(4) == 16

def test_square_perimeter():
    assert square_perimeter(4) == 16
