import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from geometric_lib.calculate import calc

def test_calc_area():
    assert calc("area", "square", 4) == 16

def test_calc_perimeter():
    assert calc("perimeter", "circle", 3) == pytest.approx(18.85, 0.01)

def test_invalid_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        calc("volume", "cube", 3)
