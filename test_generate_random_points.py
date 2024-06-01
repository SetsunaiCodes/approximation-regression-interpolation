import unittest
import random
import numpy as np
from app import generate_random_points

class TestGenerateRandomPoints(unittest.TestCase):

    def setUp(self):
        random.seed(0)
        np.random.seed(0)

    def test_generate_random_points_structure(self):
        """Testet, ob die Funktion ein Dictionary mit den Schlüsseln 'X' und 'Y' zurückgibt."""
        result = generate_random_points()
        self.assertIsInstance(result, dict)
        self.assertIn("X", result)
        self.assertIn("Y", result)
    
    def test_generate_random_points_length(self):
        """Testet, ob die Listen 'X' und 'Y' jeweils 10 Elemente enthalten."""
        result = generate_random_points()
        self.assertEqual(len(result["X"]), 10)
        self.assertEqual(len(result["Y"]), 10)

    def test_generate_random_points_value_ranges(self):
        """Testet, ob die Werte in 'X' und 'Y' in den erwarteten Bereichen liegen."""
        result = generate_random_points()
        for x in result["X"]:
            self.assertGreaterEqual(x, 0)
            self.assertLessEqual(x, 10)
        for y in result["Y"]:
            self.assertGreaterEqual(y, -0.5)
            self.assertLessEqual(y, 1.5)

if __name__ == "__main__":
    unittest.main()


## Terminal: python -m unittest test_generate_random_points.py  ##