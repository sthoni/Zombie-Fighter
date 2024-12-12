import pyxel
import movement
import time

class App:
    def __init__(self):
        pyxel.init(1024, 768)
        
        # Player 1
        self.rect_x1 = 250
        self.rect_y1 = 50

        self.velocity_p1 = 0

        self.p1IsPunching = False
        self.p1LastPunchTime = time.time() - 3 # Zeit vom letzten Schlag

        # Player 2
        self.rect_x2 = 750
        self.rect_y2 = 50

        self.velocity_p2 = 0
        
        self.gravity = 1

        self.p2IsPunching = False
        self.p2LastPunchTime = time.time() - 3 # Zeit vom letzten Schlag

        self.backgroundColor = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        
        #Gravitation

        self.rect_y1, self.velocity_p1 = movement.gravitation(self.rect_y1, pyxel.height, self.gravity, self.velocity_p1)

        self.rect_y2, self.velocity_p2 = movement.gravitation(self.rect_y2, pyxel.height, self.gravity, self.velocity_p2)


        #Movement

        self.rect_x1 = movement.movementP1(self.rect_x1)

        self.rect_x2 = movement.movementP2(self.rect_x2)


        # Schlag

        self.p1IsPunching, self.p1LastPunchTime =  movement.punch_p1(self.p1IsPunching, self.p1LastPunchTime)

        self.p2IsPunching, self.p2LastPunchTime =  movement.punch_p2(self.p2IsPunching, self.p2LastPunchTime)
        
    def draw(self):
        pyxel.cls(0)
        
        
        pyxel.rect(self.rect_x1, self.rect_y1, 100, 248, 2)

        pyxel.rect(self.rect_x2, self.rect_y2, 100, 248, 2)

        if self.p1IsPunching:
            pyxel.rect(self.rect_x1 + 160, self.rect_y1 + 5, 50, 50, 8)
        if self.p2IsPunching:
            pyxel.rect(self.rect_x2 + 160, self.rect_y2 + 5, 50, 50, 8)
        

App()