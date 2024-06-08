### Manuelle Berechnung der Regressionskoeffizienten für ersten Test

Für die Daten:


$ X = [1, 2, 3, 4, 5] $

$ Y = [2, 3, 5, 4, 6] $

Berechnung der Summe der X- und Y-Werte sowie die Summe der Produkte und Quadrate:
$$
\sum X = 1 + 2 + 3 + 4 + 5 = 15
$$

$$
\sum Y = 2 + 3 + 5 + 4 + 6 = 20
$$

$$
\sum XY = (1 \cdot 2) + (2 \cdot 3) + (3 \cdot 5) + (4 \cdot 4) + (5 \cdot 6) = 2 + 6 + 15 + 16 + 30 = 69
$$

$$
\sum X^2 = (1^2) + (2^2) + (3^2) + (4^2) + (5^2) = 1 + 4 + 9 + 16 + 25 = 55
$$

Die Koeffizienten berechnen sich dann wie folgt:

$$
a = \frac{n \sum XY - \sum X \sum Y}{n \sum X^2 - (\sum X)^2} = \frac{5 \cdot 69 - 15 \cdot 20}{5 \cdot 55 - 15^2} = \frac{345 - 300}{275 - 225} = \frac{45}{50} = 0.9
$$

$$
b = \frac{\sum Y \sum X^2 - \sum X \sum XY}{n \sum X^2 - (\sum X)^2} = \frac{20 \cdot 55 - 15 \cdot 69}{5 \cdot 55 - 15^2} = \frac{1100 - 1035}{275 - 225} = \frac{65}{50} = 1.3
$$

Sprich: Der Test der Basis funktioniert mit diesem Datenset und kann angewendet werden.
