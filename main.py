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

        # Player 2
        self.rect_x2 = 150
        self.rect_y2 = 10

        self.hp2 = 1000

        self.velocity_p2 = 0
        
        #Gravity
        self.gravity = 0.75

        #Punch
        self.p2IsPunching = False
        self.p2LastPunchTime = time.time() - 3 # Zeit vom letzten Schlag

        self.backgroundColor = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        
        # Gravitation

        self.rect_y1, self.velocity_p1 = movement.gravitation(self.rect_y1, self.gravity, self.velocity_p1)

        self.rect_y2, self.velocity_p2 = movement.gravitation(self.rect_y2, self.gravity, self.velocity_p2)


        # Movement

        self.rect_x1 = movement.movementP1(self.rect_x1)

        self.rect_x2 = movement.movementP2(self.rect_x2)

        # Jump

        if pyxel.btnp(pyxel.KEY_W):
            self.rect_y1 -= 35


        # Schlag

        self.p1IsPunching, self.p1LastPunchTime, self.hp2 =  movement.punch_p1(self.p1IsPunching, self.p1LastPunchTime, self.rect_x2, self.rect_x1, self.hp2)

        self.p2IsPunching, self.p2LastPunchTime =  movement.punch_p2(self.p2IsPunching, self.p2LastPunchTime)
        
    def draw(self):
        pyxel.cls(0)
        
        
        pyxel.rect(self.rect_x1, self.rect_y1, 32, 32, 2)

        pyxel.rect(self.rect_x2, self.rect_y2, 32, 32, 2)

        if self.p1IsPunching:
            pyxel.rect(self.rect_x1 + 40, self.rect_y1 + 5, 20, 20, 8)
            pyxel.rect(self.rect_x1 - 28, self.rect_y1 + 5, 20, 20, 8)
        if self.p2IsPunching:
            pyxel.rect(self.rect_x2 + 40, self.rect_y2 + 5, 20, 20, 8)
            pyxel.rect(self.rect_x2 - 28, self.rect_y2 + 5, 20, 20, 8)
        

App()