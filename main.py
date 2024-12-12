import pyxel
import movement
import time

class App:
    def __init__(self):
        pyxel.init(1024, 768)
        
        # Player 1
        self.rect_x1 = 250
        self.rect_y1 = 50

        # Player 2
        self.rect_x2 = 750
        self.rect_y2 = 50

        self.velocity_p1 = 0
        self.velocity_p2 = 0
        
        self.gravity = 1

        self.p1IsPunching = False
        self.p1LastPunchTime = time.time() - 3 # Zeit vom letzten Schlag
        self.p1CurrentPunchTime = 0 # Zeit vom jetzt versuchten Schlag

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

        if pyxel.btnp(pyxel.KEY_SPACE) and time.time() - self.p1LastPunchTime >= 0.5:
            print("Differenz: " , time.time() - self.p1LastPunchTime)
            self.p1IsPunching = True
            self.p1LastPunchTime = time.time()
        else: # Wir müssen Herr Thon fragen, ob das eine gute Lösung ist
            self.p1IsPunching = False
       
 

    def draw(self):
        pyxel.cls(0)
        
        
        pyxel.rect(self.rect_x1, self.rect_y1, 100, 248, 2)

        pyxel.rect(self.rect_x2, self.rect_y2, 100, 248, 2)

        if self.p1IsPunching:
            pyxel.rect(self.rect_x1 + 160, self.rect_y1 + 5, 50,50, 8)
        

App()