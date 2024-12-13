import pyxel
import time


# Movement
def movementP1(xPos):
    if pyxel.btn(pyxel.KEY_D):
        xPos += 3
    elif pyxel.btn(pyxel.KEY_A):
        xPos -= 3

    return xPos

def movementP2(xPos):
    if pyxel.btn(pyxel.KEY_RIGHT):
        xPos += 3

    elif pyxel.btn(pyxel.KEY_LEFT):
        xPos -= 3

    return xPos


#Jump aber es klappt noch nicht
def jump(yPos):
    jumpVelocity = 0

    if pyxel.btn(pyxel.KEY_W):
        yPos -= jumpVelocity

    return yPos


#Gravitation
def gravitation(rect_y, height, gravity, velocity):
    if rect_y + 45 <= 100:
        velocity += gravity
        rect_y += velocity

    if rect_y + 45 >= 100:  #248 ist die Größe vom Spieler auf der Y-Achse
        velocity = 0

    return rect_y, velocity



#Attacken
def punch_p1(p_is_punching, p_last_punch_time, enemy_x, player_x): #pIsPunching: p1_is_punching (Für Hitbox)   p_last_punch_time: Cooldoown Zeit (Letzter Schlag)
    if pyxel.btnp(pyxel.KEY_G) and time.time() - p_last_punch_time >= 0.5: # Geguckt ob G gedrückt wird und Cooldown
        p_is_punching = True #Aktiviert die Hitbox
        p_last_punch_time = time.time() # Letzter Schlag (Zeit) wird auf jetzt gesetzt

        if enemy_x > player_x + 40 and enemy_x < player_x + 60:
            print("Hit")
    
    else: # Wir müssen Herr Thon fragen, ob das eine gute Lösung ist aber ich glaube ja weil es nur einmal aufgerufen wird (1 Frame)
        p_is_punching = False
    
    return p_is_punching, p_last_punch_time #Return damit die Variable in main.py verändert wird sonst geht es nicht



#Gleiche Methode aber mit Taste 5 auf der Tastatur Rechts für Spieler 2
def punch_p2(p_is_punching, p_last_punch_time):
    if pyxel.btnp(pyxel.KEY_KP_5) and time.time() - p_last_punch_time >= 0.5:
        p_is_punching = True
        p_last_punch_time = time.time()

    else: 
        p_is_punching = False

    return p_is_punching, p_last_punch_time
