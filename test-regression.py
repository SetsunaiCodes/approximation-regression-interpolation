import unittest
import numpy as np
from equation import regression

class TestRegression(unittest.TestCase):
    
    def setUp(self):
        # Beispieldaten definieren
        self.data = {
            "X": [1, 2, 3, 4, 5, 6, 7],
            "Y": [2, 3, 5, 4, 6, 6, 7]
        }

    def test_basic_regression(self):
        # Regression mit einfach Daten testen
        x, y_prognose = regression(self.data)
        # Check nach der Länge der Daten und der Prognose
        self.assertEqual(len(x), len(y_prognose))
        # Check ob es sich bei der Prognose um INTs oder Floats handelt
        self.assertTrue(all(isinstance(i, (int, float)) for i in y_prognose))
        
    def test_empty_data(self):
        # Test mit zwei leeren Listen
        empty_data = {"X": [], "Y": []}
        x, y_prognose = regression(empty_data)
        self.assertEqual(len(x), 0)
        self.assertEqual(len(y_prognose), 0)
        
    def test_linear_data(self):
        # Test mit linearem Datensatz
        linear_data = {"X": [1, 2, 3, 4, 5], "Y": [2, 4, 6, 8, 10]}
        x, y_prognose = regression(linear_data)
        expected_y_prognose = [2, 4, 6, 8, 10]
        np.testing.assert_almost_equal(y_prognose, expected_y_prognose)

    def test_constant_data(self):
        # Test mit konstantem Datensatz
        constant_data = {"X": [1, 2, 3, 4, 5], "Y": [3, 3, 3, 3, 3]}
        x, y_prognose = regression(constant_data)
        expected_y_prognose = [3, 3, 3, 3, 3]
        np.testing.assert_almost_equal(y_prognose, expected_y_prognose)
        
    def test_single_point(self):
        # Test mit Datensatz, der nur aus einem Punkt pro Liste besteht
        single_point_data = {"X": [2], "Y": [5]}
        x, y_prognose = regression(single_point_data)
        self.assertEqual(y_prognose, [5])

if __name__ == '__main__':
    unittest.main()
