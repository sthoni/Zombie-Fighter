import pyxel
import movement
import time

class App:
    def __init__(self):
        pyxel.init(180, 100)
        
        # Player 1
        self.rect_x1 = 60
        self.rect_y1 = 10

        self.hp1 = 1000

        self.velocity_p1 = 0

        self.p1IsPunching = False
        self.p1LastPunchTime = time.time() - 3 # Zeit vom letzten Schlag

        self.p1richtung = "rechts"

        # Player 2
        self.rect_x2 = 150
        self.rect_y2 = 10

        self.hp2 = 1000

        self.velocity_p2 = 0


        self.p2richtung = "links"
        
        #Gravity
        self.gravity = 0.75

        #Punch
        self.p2IsPunching = False
        self.p2LastPunchTime = time.time() - 3 # Zeit vom letzten Schlag

        self.backgroundColor = 0
        pyxel.run(self.update, self.draw)

        self.new_hp_bar = 35


    def update(self):
        
        # Gravitation

        self.rect_y1, self.velocity_p1 = movement.gravitation(self.rect_y1, self.gravity, self.velocity_p1)

        self.rect_y2, self.velocity_p2 = movement.gravitation(self.rect_y2, self.gravity, self.velocity_p2)


        # Movement

        self.rect_x1, self.p1richtung = movement.movementP1(self.rect_x1, self.p1richtung)

        self.rect_x2, self.p2richtung = movement.movementP2(self.rect_x2, self.p2richtung)

        # Jump

#        if pyxel.btnp(pyxel.KEY_W):
#            self.rect_y1 -= 35


        # Schlag

        self.p1IsPunching, self.p1LastPunchTime, self.hp2 =  movement.punch_p1(self.p1IsPunching, self.p1LastPunchTime, self.rect_x2, self.rect_x1, self.hp2)

        


        self.p2IsPunching, self.p2LastPunchTime =  movement.punch_p2(self.p2IsPunching, self.p2LastPunchTime, self.rect_x1, self.rect_x1, self.hp1)
        
    def draw(self):
        pyxel.cls(0)
        
        #Spieler 1

        pyxel.rect(self.rect_x1, self.rect_y1, 32, 32, 2)

        if self.p1richtung == "rechts":
            pyxel.rect(self.rect_x1 +30, self.rect_y1 + 4, 2,2 ,0)

        if self.p1richtung == "links":
            pyxel.rect(self.rect_x1, self.rect_y1 + 4, 2,2 ,0)


        #Spieler 2

        pyxel.rect(self.rect_x2, self.rect_y2, 32, 32, 2)

        if self.p2richtung == "rechts":
            pyxel.rect(self.rect_x2 +30, self.rect_y2 + 4, 2,2 ,0)

        if self.p2richtung == "links":
            pyxel.rect(self.rect_x2 , self.rect_y2 + 4, 2,2 ,0)


        # HP bar for Player 2
        pyxel.rect(120, 7, 1000 / 22, 5, 8)
        pyxel.rect(120, 7, self.hp2 / 22, 5, 3)

        if self.p1IsPunching:
            pyxel.rect(self.rect_x1 + 40, self.rect_y1 + 5, 20, 20, 8)
            pyxel.rect(self.rect_x1 - 28, self.rect_y1 + 5, 20, 20, 8)

        if self.p2IsPunching:
            pyxel.rect(self.rect_x2 + 40, self.rect_y2 + 5, 20, 20, 8)
            pyxel.rect(self.rect_x2 - 28, self.rect_y2 + 5, 20, 20, 8)
        

App()