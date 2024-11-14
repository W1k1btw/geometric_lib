import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../geometric_lib')))
from .square import square_area, square_perimeter

def test_square_area():
    assert square_area(4) == 16

def test_square_perimeter():
    assert square_perimeter(4) == 16
