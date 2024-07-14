import numpy as np;

# Regression:
################################################################################################

def regression(data):

    # Dynamisch Länge von X zwischenspeichern
    length = len(data["X"])
    
    # Überprüfung für weniger als zwei Datenpunkte
    if length < 2:
        return data["X"], data["Y"]
    
    # Konvertieren der Listen zu Arrays, weil Numpy dann damit rechnen kann (Numpy hat issues mit Listen).
    x = np.array(data["X"])
    y = np.array(data["Y"])

    # Mittelwert berechnen
    MittelwertX = np.mean(x)
    MittelwertY = np.mean(y)

    
    # Summe aus (x - dem Mittelwert)^2
    Sx = np.sum((x - MittelwertX) ** 2)
    Sy = np.sum((y - MittelwertY) ** 2)


    # Standardabweichung
    StandardabweichungX = np.sqrt(Sx / length)
    StandardabweichungY = np.sqrt(Sy / length)


    # Kovarianz
    xy = np.sum((x - MittelwertX) * (y - MittelwertY))
    Kovarianz = xy / length

    # Korrelationskoeffizient
    Korrelation = Kovarianz / (StandardabweichungX * StandardabweichungY)
    
    b = Kovarianz / Sx * length
    a = MittelwertY - b * MittelwertX
    
    # Definieren der Prognose
    yPrognose = [b * xi + a for xi in x]

    return x, yPrognose


# Interpolation:
################################################################################################
def interpolation(data):
    x = np.array(data["X"])
    y = np.array(data["Y"])

    # Überprüfen, ob die Eingabedaten leer sind
    if len(x) == 0 or len(y) == 0:
        return x, y

    f = np.interp(x, x, y)

    return x, f