import pyxel
import time

speed = 4

# Movement
def movementP1(xPos, richtung):
    if pyxel.btn(pyxel.KEY_D):
            if xPos <= 180 - 32:
                xPos += speed 
                richtung = "rechts"
    elif pyxel.btn(pyxel.KEY_A):
        if xPos >= 0:
            xPos -= speed 
            richtung = "links"

    return xPos, richtung

def movementP2(xPos, richtung):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if xPos <= 180 - 32:
            xPos += speed
            richtung = "rechts"
    elif pyxel.btn(pyxel.KEY_LEFT):
        if xPos >= 0:
            xPos -= speed 
            richtung = "links"

    return xPos, richtung


#Jump aber es klappt noch nicht
def jump(yPos):
    jumpVelocity = 0

    if pyxel.btn(pyxel.KEY_W):
        yPos -= jumpVelocity

    return yPos


#Gravitation
def gravitation(rect_y, gravity, velocity):
    if rect_y + 45 <= 100:
        velocity += gravity
        rect_y += velocity

    if rect_y + 45 >= 100:  #248 ist die Größe vom Spieler auf der Y-Achse
        velocity = 0

    return rect_y, velocity



#Attacken
def punch_p1(p_is_punching, p_last_punch_time, enemy_x, player_x, hp2): #pIsPunching: p1_is_punching (Für Hitbox)   p_last_punch_time: Cooldoown Zeit (Letzter Schlag)
    if pyxel.btnp(pyxel.KEY_G) and time.time() - p_last_punch_time >= 0.5: # Geguckt ob G gedrückt wird und Cooldown
        p_is_punching = True #Aktiviert die Hitbox
        p_last_punch_time = time.time() # Letzter Schlag (Zeit) wird auf jetzt gesetzt

        if collision(player_x, enemy_x):
            hp2 -= 80
            print(hp2)

        if collision(player_x - 68, enemy_x):
            print("Collsion")

    
    else: # Wir müssen Herr Thon fragen, ob das eine gute Lösung ist aber ich glaube ja weil es nur einmal aufgerufen wird (1 Frame)
        p_is_punching = False
    
    return p_is_punching, p_last_punch_time, hp2 #Return damit die Variable in main.py verändert wird sonst geht es nicht



#Gleiche Methode aber mit Taste 5 auf der Tastatur Rechts für Spieler 2
def punch_p2(p_is_punching, p_last_punch_time, enemy_x, player_x, hp2):
    if pyxel.btnp(pyxel.KEY_KP_5) and time.time() - p_last_punch_time >= 0.5:
        p_is_punching = True
        p_last_punch_time = time.time()

        if collision(player_x, enemy_x):
            hp2 - 80
            print("fuhebhfbh")

    else: 
        p_is_punching = False

    return p_is_punching, p_last_punch_time

def collision(player_x, enemy_x):
    if enemy_x >= player_x + 40 and enemy_x <= player_x + 60 or enemy_x < player_x + 40 and enemy_x + 32 > player_x + 60:
        print("Hit")
        return True
    