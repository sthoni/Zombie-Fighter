import pyxel
import movement

class App:
    def __init__(self):
        pyxel.init(1024, 768)
        self.rect_x = 248
        self.rect_y = 50

        self.velocity = 0
        self.gravity = 1

        self.backgroundColor = 0
        pyxel.run(self.update, self.draw)


    def update(self):
        
        #Gravitation
        self.velocity += self.gravity
        self.rect_y += self.velocity

        if self.rect_y + 248 >= pyxel.height:  #248 is how big the player on the y axe is
            self.rect_y = pyxel.height - 248
            self.velocity = 0
        
        #Movement
        self.rect_x = movement.movementP1(self.rect_x)

        if self.rect_y == 768 - 248:
            self.rect_y = movement.jump(self.rect_y)
 

    def draw(self):
        pyxel.cls(0)
        
        
        pyxel.rect(self.rect_x, self.rect_y, 100, 248, 2)
        

App()