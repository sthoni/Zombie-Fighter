import pyxel
import movement
import time

class App:
    def __init__(self):
        pyxel.init(1024, 768)
        self.rect_x = 248
        self.rect_y = 50

        self.velocity = 0
        self.gravity = 1

        self.p1IsPunching = False
        self.p1LastPunchTime = 0 # Zeit vom letzten Schlag
        self.p1CurrentPunchTime = 0 # Zeit vom jetzt versuchten Schlag

        self.backgroundColor = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        
        #Gravitation

        self.velocity += self.gravity
        self.rect_y += self.velocity

        if self.rect_y + 248 >= pyxel.height:  #248 ist die Größe vom Spieler auf der Y-Achse
            self.rect_y = pyxel.height - 248
            self.velocity = 0
        


        #Movement

        self.rect_x = movement.movementP1(self.rect_x)

        if self.rect_y == 768 - 248:
            self.rect_y = movement.jump(self.rect_y)



        # Schlag

        if pyxel.btnp(pyxel.KEY_SPACE) and int(time.time()) - self.p1LastPunchTime >= 1:
            print("Differenz: " , int(time.time()) - self.p1LastPunchTime)
            self.p1IsPunching = True
            self.p1LastPunchTime = int(time.time())
        else: # Wir müssen Herr Thon fragen, ob das eine gute Lösung ist
            self.p1IsPunching = False


            
 

    def draw(self):
        pyxel.cls(0)
        
        
        pyxel.rect(self.rect_x, self.rect_y, 100, 248, 2)

        if self.p1IsPunching:
            pyxel.rect(self.rect_x + 160, self.rect_y + 5, 50,50, 8)
        

App()