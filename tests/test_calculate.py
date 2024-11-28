import unittest
from geometric_lib.calculate import calc

class CalculateTestCase(unittest.TestCase):
    
    def test_calc_area(self):
        # Проверяем расчет площади квадрата
        self.assertEqual(calc("square", "area", [4]), 16)

    def test_calc_perimeter(self):
        # Проверяем расчет периметра круга
        self.assertAlmostEqual(calc("circle", "perimeter", [3]), 18.85, places=2)

    def test_invalid_operation(self):
        # Проверяем, что при попытке вызвать несуществующую операцию выбрасывается исключение
        with self.assertRaises(ValueError) as context:
            calc("circle", "volume", [3])
        self.assertEqual(str(context.exception), "Unsupported function")
        
    def test_invalid_figure(self):
        # Проверяем, что при передаче несуществующей фигуры выбрасывается исключение
        with self.assertRaises(ValueError) as context:
            calc("hexagon", "area", [5])
        self.assertEqual(str(context.exception), "Unsupported figure")
    
    def test_invalid_size(self):
        # Проверяем передачу неверных аргументов для расчета
        with self.assertRaises(TypeError):
            calc("square", "area", "invalid")
        
if __name__ == "__main__":
    unittest.main()
