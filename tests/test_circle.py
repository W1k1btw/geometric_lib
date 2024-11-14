import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../geometric_lib')))
from geometric_lib.circle import circle_area, circle_perimeter

def test_circle_area():
    assert pytest.approx(circle_area(3), 0.01) == 28.27

def test_circle_perimeter():
    assert pytest.approx(circle_perimeter(3), 0.01) == 18.85
