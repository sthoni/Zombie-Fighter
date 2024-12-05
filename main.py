import pyxel

class App:
    def __init__(self):
        pyxel.init(1024, 768)
        self.rect_x = 248
        self.rect_y = 248
        
        self.rect_xx = 100
        self.rect_yy = 100
        
        self.rect_color = 2
        
        self.backgroundColor = 0
        pyxel.run(self.update, self.draw)

    def update(self):

        if self.rect_y < 768 - 248:
            self.rect_y +=10

        if self.rect_yy < 768 - 248:
            self.rect_yy += 10

        if pyxel.btn(pyxel.KEY_D):
            if self.rect_x < pyxel.width - 100:
                self.rect_x += 20
        if pyxel.btn(pyxel.KEY_A):
            if self.rect_x > 0:
                self.rect_x += -20
        if pyxel.btn(pyxel.KEY_S):   
            pass
        if pyxel.btn(pyxel.KEY_W):   
            pass
                
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.rect_xx < pyxel.width - 100:
                self.rect_xx += 10
            print("Rechts")
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.rect_xx > 0:
                self.rect_xx += -10
            print("Links")
        if pyxel.btn(pyxel.KEY_DOWN):   
            pass
        if pyxel.btn(pyxel.KEY_UP):   
            pass

                
        
        

    def draw(self):
        pyxel.cls(0)
        
        
        pyxel.rect(self.rect_x, self.rect_y, 100, 248, self.rect_color)
        
        pyxel.rect(self.rect_xx, self.rect_yy, 100, 248, 7)

App()