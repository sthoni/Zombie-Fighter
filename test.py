import pyxel

# Initialwerte
x = 50  # Position des Spielers
y = 50
velocity = 0  # Anfangsgeschwindigkeit (0, weil wir starten und die Schwerkraft anwenden wollen)
gravity = 0.5  # Schwerkraft (Beschleunigung pro Frame)

def update():
    global y, velocity
    # Schwerkraft anwenden (Beschleunigung auf die Geschwindigkeit)
    velocity += gravity

    # Position basierend auf der Geschwindigkeit ändern
    y += velocity

    # Wenn der Spieler den Boden erreicht, stoppen wir ihn
    if y >= pyxel.height - 8:  # Angenommene Bodenhöhe (kann angepasst werden)
        y = pyxel.height - 8
        velocity = 0  # Geschwindigkeit zurücksetzen, wenn er den Boden berührt

def draw():
    pyxel.cls(0)
    pyxel.rect(x, y, 8, 8, 9)  # Zeichnet den Spieler als kleines Rechteck

pyxel.init(160, 120)
pyxel.run(update, draw)