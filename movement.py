import pyxel
import time

# Movement
def movementP1(xPos, richtung, state, speed, is_moving):
    
    if pyxel.btn(pyxel.KEY_D):
        is_moving = True
        if xPos <= 180 - 32:
            #if state == "blocking":
            #    xPos += speed_block
            if state == "normal":
                xPos += speed 
            richtung = "right"
    elif pyxel.btn(pyxel.KEY_A):
        is_moving = True
        if xPos >= 0:
            #if state == "blocking":
            #    xPos -= speed_block
            if state == "normal":
                xPos -= speed 
            richtung = "left"
    else:
        is_moving = False

    return xPos, richtung, is_moving

def movementP2(xPos, richtung, state, speed, is_moving):
    if pyxel.btn(pyxel.KEY_RIGHT):
        is_moving = True
        if xPos <= 180 - 32:
            if state == "normal":
                xPos += speed
            richtung = "right"
    elif pyxel.btn(pyxel.KEY_LEFT):
        is_moving = True
        if xPos >= 0:
            if state == "normal":
                xPos -= speed 
            richtung = "left"
    else:
        is_moving = False

    return xPos, richtung, is_moving

def jump(rect_y, last_jump_time):
    
    if rect_y == 59.5 and time.time() - last_jump_time > 0.5:
        last_jump_time = time.time()
        rect_y -= 20

    
    return rect_y, last_jump_time


#Gravitation
def gravitation(rect_y, velocity, gravity):
    if rect_y + 45 <= 100:
        velocity += gravity
        rect_y += velocity

    if rect_y + 45 >= 100:  #248 ist die Größe vom Spieler auf der Y-Achse
        velocity = 0

    return rect_y, velocity

#Attacken
def punch_p1(self, p_is_punching, p_last_punch_time, enemy_x, player_x, hp2): #pIsPunching: p1_is_punching (Für Hitbox)   p_last_punch_time: Cooldoown Zeit (Letzter Schlag)
    if pyxel.btnp(pyxel.KEY_SPACE) and time.time() - p_last_punch_time >= 0.5: # Geguckt ob G gedrückt wird und Cooldown
        p_is_punching = True #Aktiviert die Hitbox
        p_last_punch_time = time.time() # Letzter Schlag (Zeit) wird auf jetzt gesetzt

        if collision_rechts(player_x, enemy_x):
            if self.state_player_2 == "normal" and self.state_player_1 == "normal" and self.p1_direction == "right":
                hp2 -= 80
                pyxel.play(3,51)
                self.rect_x2 += 6
            elif self.state_player_2 == "blocking" and self.state_player_1 == "normal" and self.p1_direction == "right":
                hp2 -= 10
                pyxel.play(3,51)
                self.rect_x2 += 2
            print("P2: " , hp2)
            print("Rechts")

        if collision_links(player_x, enemy_x):
            if self.state_player_2 == "normal" and self.state_player_1 == "normal" and self.p1_direction == "left":
                hp2 -= 80
                pyxel.play(3,51)
                self.rect_x2 -= 6
            elif self.state_player_2 == "blocking" and self.state_player_1 == "normal" and self.p1_direction == "left":
                hp2 -= 10
                pyxel.play(3,51)
                self.rect_x2 -= 2
            print("P2: " , hp2)
            print("Links")

    
    else: # Wir müssen Herr Thon fragen, ob das eine gute Lösung ist aber ich glaube ja weil es nur einmal aufgerufen wird (1 Frame)
        p_is_punching = False
    
    return p_is_punching, p_last_punch_time, hp2, self #Return damit die Variable in main.py verändert wird sonst geht es nicht



#Gleiche Methode aber mit Taste 5 auf der Tastatur Rechts für Spieler 2
def punch_p2(self, p_is_punching, p_last_punch_time, enemy_x, player_x, hp1):
    if pyxel.btnp(pyxel.KEY_KP_0) and time.time() - p_last_punch_time >= 0.5:
        p_is_punching = True
        
        p_last_punch_time = time.time()

        if collision_rechts(player_x, enemy_x):
            if self.state_player_1 == "normal" and self.state_player_2 == "normal" and self.p2_direction == "right":
                hp1 -= 80
                pyxel.play(2,50)
                self.rect_x1 += 6
            elif self.state_player_1 == "blocking" and self.state_player_2 == "normal" and self.p2_direction == "right":
                hp1 -= 10
                pyxel.play(2,50)
                self.rect_x1 += 2
            print("P1: ", hp1)
            print("Rechts")
        
        if collision_links(player_x, enemy_x):
            if self.state_player_1 == "normal" and self.state_player_2 == "normal" and self.p2_direction == "left":
                hp1 -= 80
                pyxel.play(2,50)
                self.rect_x1 -= 6
            elif self.state_player_1 == "blocking" and self.state_player_2 == "normal" and self.p2_direction == "left":
                hp1 -= 10
                pyxel.play(2,50)
                self.rect_x1 -= 2
            print("P1: " , hp1)
            print("Links")

    else: 
        p_is_punching = False

    return p_is_punching, p_last_punch_time, hp1, self

def collision_rechts(player_x, enemy_x):
    if enemy_x >= player_x + 16 and enemy_x <= player_x + 26 or enemy_x < player_x + 36 and enemy_x + 40 > player_x + 25:
        return True
    
def collision_links(player_x, enemy_x):
    if enemy_x >= player_x - 10 and enemy_x <= player_x or enemy_x < player_x -10 and enemy_x + 28 > player_x -10:
        return True