import unittest
import numpy as np
from equation import interpolation

class TestInterpolation(unittest.TestCase):
    
    def setUp(self):
        # Set up some example data to use in tests
        self.data = {
            "X": [1, 2, 3, 4, 5, 6, 7],
            "Y": [2, 3, 5, 4, 6, 6, 7]
        }

    def test_basic_interpolation(self):
        # Test the interpolation function with example data
        x, y_interpolated = interpolation(self.data)
        self.assertEqual(len(x), len(y_interpolated))
        self.assertTrue(all(isinstance(i, (int, float)) for i in y_interpolated))
        # Desired Output: The lengths of x and y_interpolated should match, 
        # and all elements in y_interpolated should be either int or float

    def test_empty_data(self):
        # Test with empty data
        empty_data = {"X": [], "Y": []}
        x, y_interpolated = interpolation(empty_data)
        self.assertEqual(len(x), 0)
        self.assertEqual(len(y_interpolated), 0)
        # Desired Output: Both x and y_interpolated should be empty lists

    def test_linear_interpolation(self):
        # Test with linear data
        linear_data = {"X": [1, 2, 3, 4, 5], "Y": [2, 4, 6, 8, 10]}
        x, y_interpolated = interpolation(linear_data)
        expected_y_interpolated = [2, 4, 6, 8, 10]
        np.testing.assert_almost_equal(y_interpolated, expected_y_interpolated)
        # Desired Output: y_interpolated should match exactly with the expected_y_interpolated

if __name__ == '__main__':
    unittest.main()
