import unittest
import numpy as np
from equation import interpolation

class TestInterpolation(unittest.TestCase):
    
    def setUp(self):
        # Beispieldaten definieren
        self.data = {
            "X": [1, 2, 3, 4, 5, 6, 7],
            "Y": [2, 3, 5, 4, 6, 6, 7]
        }

    def test_basic_interpolation(self):
        x, y_interpolated = interpolation(self.data)
        self.assertEqual(len(x), len(y_interpolated))
        self.assertTrue(all(isinstance(i, (int, float)) for i in y_interpolated))

    def test_empty_data(self):
        # Test mit leerem Datensatz
        empty_data = {"X": [], "Y": []}
        x, y_interpolated = interpolation(empty_data)
        self.assertEqual(len(x), 0)
        self.assertEqual(len(y_interpolated), 0)


    def test_linear_interpolation(self):
        # Test mit linearem Datensatz
        linear_data = {"X": [1, 2, 3, 4, 5], "Y": [2, 4, 6, 8, 10]}
        x, y_interpolated = interpolation(linear_data)
        expected_y_interpolated = [2, 4, 6, 8, 10]
        np.testing.assert_almost_equal(y_interpolated, expected_y_interpolated)

if __name__ == '__main__':
    unittest.main()
