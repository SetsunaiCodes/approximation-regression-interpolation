import unittest
import numpy as np

# Funktion calculate_manual_regression
def calculate_manual_regression(data):
    X = np.array(data["X"])
    Y = np.array(data["Y"])
    n = len(X)
    
    sum_X = np.sum(X)
    sum_Y = np.sum(Y)
    sum_XY = np.sum(X * Y)
    sum_X2 = np.sum(X ** 2)
    
    nenner = n * sum_X2 - sum_X ** 2
    if nenner == 0:
        #Nenner meint hier den obere Bereich der Ausgangsfunktion
        #Edgecase
        raise ValueError("Der Nenner ist 0. Regression kann nicht berechnet werden.")
    
    a = (n * sum_XY - sum_X * sum_Y) / nenner
    b = (sum_Y * sum_X2 - sum_X * sum_XY) / nenner
    
    return a, b

class TestCalculateManualRegression(unittest.TestCase):
    # Normaler Case
    def test_basic_case(self):
        data = {
            "X": [1, 2, 3, 4, 5],
            "Y": [2, 3, 5, 4, 6]
        }
        a, b = calculate_manual_regression(data)
        # Erwartete Regressionskoeffizienten (die hab ich auch händisch)
        # "Almost" weil hier floats rauskommen
        self.assertAlmostEqual(a, 0.9, places=1)
        self.assertAlmostEqual(b, 1.3, places=1)
    
    # Perfekter Fit für eine gerade Regressionslinie
    def test_perfect_fit(self):
        data = {
            "X": [1, 2, 3, 4, 5],
            "Y": [2, 4, 6, 8, 10]
        }
        a, b = calculate_manual_regression(data)
        # Erwartete Regressionskoeffizienten
        self.assertEqual(a, 2)
        self.assertEqual(b, 0)

    # Testet die Funktion mit einem Datensatz, der eine negative Steigung hat (Y=−2X). 
    # Die erwarteten Werte für a und b sind -2 und 12.
    def test_negative_slope(self):
        data = {
            "X": [1, 2, 3, 4, 5],
            "Y": [10, 8, 6, 4, 2]
        }
        a, b = calculate_manual_regression(data)
        # Erwartete Regressionskoeffizienten
        self.assertEqual(a, -2)
        self.assertEqual(b, 12)
    
    # Test wenn jewelis nur ein Punkt im Dictionary ist (Es wird kein Ergebnis erziehlt, wenn dieser Fall eintritt)
    def test_single_point(self):
        data = {
            "X": [1],
            "Y": [2]
        }
        #Fehlermeldung ausliefern
        with self.assertRaises(ValueError) as context:
            calculate_manual_regression(data)
        self.assertTrue("Nenner ist 0" in str(context.exception))
    
    # Test wenn durch die Werte eine gerade Linie gezogen wird (Es wird kein Ergebnis erziehlt, wenn dieser Fall eintritt)
    def test_vertical_line(self):
        data = {
            "X": [1, 1, 1, 1, 1],
            "Y": [2, 3, 4, 5, 6]
        }
        #Fehlermeldung ausliefern
        with self.assertRaises(ValueError) as context:
            calculate_manual_regression(data)
        self.assertTrue("Nenner ist 0" in str(context.exception))

if __name__ == '__main__':
    unittest.main()

# Funktion besteht alle Tests.