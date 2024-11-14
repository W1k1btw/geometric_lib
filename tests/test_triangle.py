import pytest
from .triangle import triangle_area, triangle_perimeter

def test_triangle_area():
    assert triangle_area(3, 4, 5) == 6

def test_triangle_perimeter():
    assert triangle_perimeter(3, 4, 5) == 12
