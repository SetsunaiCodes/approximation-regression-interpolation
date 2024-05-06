#Hier werden alle Rechnungen angefertigt


# Daten als Dictionary
data = {
    "X": [1, 2, 3, 4, 5, 4, 5],
    "Y": [2, 3, 5, 4, 6, 6, 7]
}
# unabhängige Variable
x = data["X"]
# abhängige Variable
y = data["Y"]


###  Mittelwert berechnen  ###

# Summe aller Werte / Anzahl an Werten
MittelwertX = sum(x) / len(x)
MittelwertY = sum(y) / len(y)
# Mittelwert einer Liste mit numpy berechnen:   numpy.mean(X)
# Mittelwert mit statistics berechnen:          statistics.mean(list)



###  Steigung (m)  ###

Sx = 0
Sxy = 0

for i in x:
    Sx += (x[i] - MittelwertX)**2 
    # Alternativen zum quadrieren: pow() und math.pow()

for i in x:
    Sxy += (x[i] - MittelwertX)**2 * (y[i] - MittelwertY)**2


Steigung = Sx / Sxy


###  Konstante => y-Achsenabschnitt  ###

# -> Konstante = Steigung * x[i] + y[i]

sumKonst = 0
for i in x:
    Konstante = Steigung * x[i] + y[i]
    print(f'xi: {x[i]}  yi: {y[i]} Konstante: {Konstante}')
    sumKonst += Konstante

Konstante=sumKonst/len(x)
print(Konstante)


###  lineare Regressionsgrade  ###
# y = m*x + b




# Anleitung Interpolation: https://www.w3schools.com/python/scipy/scipy_interpolation.php


