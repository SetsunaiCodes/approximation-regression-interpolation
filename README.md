# Installationsanleitung

## Table of contents
- [Einleitung](#einleitung)
- [Cloning](#cloning)
- [Manueller Download](#manueller-download)
- [Dependencies und Packages](#dependencies-und-packages)
- [Ausführen](#ausführen)
- [Testing der Funktionen](#testing-der-funktionen)

## Einleitung
Sion ist ein Visualisierungswerkzeug, geschrieben in Python in Kombination mit dem Visualisierungs-Framework Dash, um interagierbare Graphen zu generieren. Sion speichert zwei Listen, die während der Laufzeit immer wieder von der Anwendung manipuliert werden.

## Cloning
> 📘 Info
> 
> Für diese Sektion wird eine Installation des Versionskontrollsystems [Git](https://git-scm.com/) vorausgesetzt.


![Clone HTTPS from GitHub](/media/CloneGitHub.png)
Sion kann über den HTTPS Key des Repositories auf ein lokales System gecloned werden. Hierfür muss die URL kopiert werden, die sich nach einem Klick auf Code im Tab local kopiert werden.

```bash
git clone <HTTPS-URL>
```
Als nächstes muss dieser Terminal Command ausgeführt werden, um das Porjekt im **aktuellen Verzeichnis** einzusetzen. So wird eine lokale Kopie des Repositories auf dem System installiert.

## Manueller Download
Alternativ lässt sich das Projekt als ZIP-Datei herunterladen, indem auf den Button "Code" geklickt wird und daraufhin die Download ZIP Variante gewählt wird.

## Dependencies und Packages
> 📘 Info
> 
> Für diese Sektion wird eine lokale Installation der Programmiersprache [Python](https://www.python.org/) vorausgesetzt, da nun der Packagemanager **pip** verwendet wird.

Um Sion erfolgreich ausführen zu können, müssen zunächst folgende Dependencies auf dem Gerät installiert sein:

- Dash
- Plotly
- Numpy
- Flask
- Statsmodels API


Sind diese Dependencies nicht installiert, können diese über den Terminal Command im **Host Verzeichnis** des Systems installiert werden:
```bash

pip install dash
pip install plotly
pip install flask
pip install numpy
pip install statsmodels

```

## Ausführen
> 📘 Info
> 
> Um den Code des Projekts einzusehen wird eine IDE empfohlen. Hierfür kann [VSCode](https://code.visualstudio.com/) verwendet werden. 

Im Verzeichnis des Repositories kann eine lokale Variante der Anwendung num mit folgendem Command gestartet werden:
```bash
python app.py
```

Im Terminal erscheint eine URL die mit STRG+Klick im Browser geöffnet wird.

## Testing der Funkionen
Um die Unittests auszuführen können folgende Terminal Commands verwendet werden:
```bash
python -m unittest <Name der Datei>

# z.B. test_generate_random_points.py
# z.B. test_generate_linear.py
```


