import pyxel
import time


# Movement Spieler 1
def movementP1(xPos, richtung, state, speed, is_moving):
    
    if pyxel.btn(pyxel.KEY_D): # rechts bewegen
        is_moving = True
        if xPos <= 180 - 32:
            if state == "normal":
                xPos += speed 
            richtung = "right"
    elif pyxel.btn(pyxel.KEY_A): # links bewegen
        is_moving = True
        if xPos >= 0:
            if state == "normal":
                xPos -= speed 
            richtung = "left"
    else: # wenn er sich überhaupt nicht bewegt
        is_moving = False

    return xPos, richtung, is_moving


# Movement Spieler 2
def movementP2(xPos, richtung, state, speed, is_moving):

    if pyxel.btn(pyxel.KEY_RIGHT): # rechts bewegen
        is_moving = True
        if xPos <= 180 - 32:
            if state == "normal":
                xPos += speed
            richtung = "right"
    elif pyxel.btn(pyxel.KEY_LEFT): # links bewegen
        is_moving = True
        if xPos >= 0:
            if state == "normal":
                xPos -= speed 
            richtung = "left"
    else: # wenn er sich überhaupt nicht bewegt
        is_moving = False

    return xPos, richtung, is_moving


# Springen
def jump(rect_y, last_jump_time):
    
    if rect_y == 59.5 and time.time() - last_jump_time > 0.5:
        last_jump_time = time.time()
        rect_y -= 20
    
    return rect_y, last_jump_time


# Schwerkraft
def gravitation(rect_y, velocity, gravity):
    if rect_y + 45 <= 100:
        velocity += gravity
        rect_y += velocity

    if rect_y + 45 >= 100:  #248 ist die Größe vom Spieler auf der Y-Achse
        velocity = 0

    return rect_y, velocity


# Attacke Player 1
def punch_p1(self, p_is_punching, p_last_punch_time, enemy_x, player_x, hp2): # pIsPunching: p1_is_punching (Für Hitbox)   p_last_punch_time: Cooldoown Zeit (Letzter Schlag)
    if pyxel.btnp(pyxel.KEY_SPACE) and time.time() - p_last_punch_time >= 0.5: # Geguckt ob G gedrückt wird und Cooldown
        p_is_punching = True # Aktiviert die Hitbox
        p_last_punch_time = time.time() # Letzter Schlag (Zeit) wird auf jetzt gesetzt

        if collision_right(player_x, enemy_x): # Kollision rechts
            if self.state_player_2 == "normal" and self.state_player_1 == "normal" and self.p1_direction == "right":
                hp2 -= 80
                self.player2_hitted = True
                pyxel.play(3,51)
                self.rect_x2 += 6
            elif self.state_player_2 == "blocking" and self.state_player_1 == "normal" and self.p1_direction == "right":
                hp2 -= 10
                self.player2_hitted = True
                pyxel.play(3,51)
                self.rect_x2 += 2

        if collision_left(player_x, enemy_x): # Kollision links
            if self.state_player_2 == "normal" and self.state_player_1 == "normal" and self.p1_direction == "left":
                hp2 -= 80
                self.player2_hitted = True
                pyxel.play(3,51)
                self.rect_x2 -= 6
            elif self.state_player_2 == "blocking" and self.state_player_1 == "normal" and self.p1_direction == "left":
                hp2 -= 10
                self.player2_hitted = True
                pyxel.play(3,51)
                self.rect_x2 -= 2
  
    else:
        p_is_punching = False
    
    return p_is_punching, p_last_punch_time, hp2, self


# Attacke Player 2
def punch_p2(self, p_is_punching, p_last_punch_time, enemy_x, player_x, hp1):
    if pyxel.btnp(pyxel.KEY_KP_0) and time.time() - p_last_punch_time >= 0.5:
        p_is_punching = True
        
        p_last_punch_time = time.time()

        if collision_right(player_x, enemy_x): # Kollision rechts
            if self.state_player_1 == "normal" and self.state_player_2 == "normal" and self.p2_direction == "right":
                hp1 -= 80
                self.player1_hitted = True
                pyxel.play(2,50)
                self.rect_x1 += 6
            elif self.state_player_1 == "blocking" and self.state_player_2 == "normal" and self.p2_direction == "right":
                hp1 -= 10
                self.player1_hitted = True
                pyxel.play(2,50)
                self.rect_x1 += 2
        
        if collision_left(player_x, enemy_x): # Kollision links
            if self.state_player_1 == "normal" and self.state_player_2 == "normal" and self.p2_direction == "left":
                hp1 -= 80
                self.player1_hitted = True
                pyxel.play(2,50)
                self.rect_x1 -= 6
            elif self.state_player_1 == "blocking" and self.state_player_2 == "normal" and self.p2_direction == "left":
                hp1 -= 10
                self.player1_hitted = True
                pyxel.play(2,50)
                self.rect_x1 -= 2

    else: 
        p_is_punching = False

    return p_is_punching, p_last_punch_time, hp1, self


def collision_right(player_x, enemy_x): # Kollision rechts
    if enemy_x >= player_x and enemy_x <= player_x +28:
        return True


def collision_left(player_x, enemy_x): # Kollision links
    if enemy_x >= player_x -28 and enemy_x <= player_x:
        return True