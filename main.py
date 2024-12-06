import pyxel
import movement

class App:
    def __init__(self):
        pyxel.init(1024, 768)
        self.rect_x = 248
        self.rect_y = 248
        
        self.backgroundColor = 0
        pyxel.run(self.update, self.draw)

        return self.rect_x

    def update(self):

        if self.rect_y < 768 - 248:
            self.rect_y +=10

        self.rect_x = movement.movementP1(self.rect_x)

        
        

    	

    def draw(self):
        pyxel.cls(0)
        
        
        pyxel.rect(self.rect_x, self.rect_y, 100, 248, 2)
        

App()