import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(-1,-1), -2)
        self.assertEqual(self.calc.add(1,-1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,2), 1)
        self.assertEqual(self.calc.subtract(2,2), 0)
        self.assertEqual(self.calc.subtract(1,-1), 2)
        self.assertEqual(self.calc.subtract(-1,-1), 0)
        self.assertEqual(self.calc.subtract(-1,1), -2)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3,2), 6)
        self.assertEqual(self.calc.multiply(1,-1), -1)
        self.assertEqual(self.calc.multiply(-1,1), -1)
        self.assertEqual(self.calc.multiply(-1,-1), 1)

    def test_division(self):
        self.assertEqual(self.calc.divide(3,2), 1.5)
        self.assertEqual(self.calc.divide(2,2), 1)
        self.assertEqual(self.calc.divide(2,-2), -1)
        self.assertEqual(self.calc.divide(-2,2), -1)
        self.assertEqual(self.calc.divide(-2,-2), 1)
