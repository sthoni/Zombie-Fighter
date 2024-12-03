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
        
        if pyxel.btn(pyxel.KEY_D):
            if self.rect_x < pyxel.width - 8 - 1:
                self.rect_x += 1
        if pyxel.btn(pyxel.KEY_S):   
            if self.rect_y < pyxel.height - 8- 1:
                self.rect_y += 1
        if pyxel.btn(pyxel.KEY_A):
            if self.rect_x > 0 + 1:
                self.rect_x += -1
        if pyxel.btn(pyxel.KEY_W):   
            if self.rect_y > 0 + 1:
                self.rect_y += -1
            
        if self.rect_color < 15:
            self.rect_color += 1
        else:
            self.rect_color = 0
            
            
            
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.rect_xx < pyxel.width - 8 - 1:
                self.rect_xx += 10
        if pyxel.btn(pyxel.KEY_DOWN):   
            if self.rect_yy < pyxel.height - 8- 1:
                self.rect_yy += 10
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.rect_xx > 0 + 1:
                self.rect_xx += -10
        if pyxel.btn(pyxel.KEY_UP):   
            if self.rect_yy > 0 + 1:
                self.rect_yy += -10
                
                
        if self.rect_xx >= self.rect_x - 8 and self.rect_xx < self.rect_x + 8 and self.rect_yy >= self.rect_y - 8 and self.rect_yy < self.rect_y + 8:
            self.backgroundColor = 8
        else:
            self.backgroundColor = 0
        

    def draw(self):
        pyxel.cls(0)
        
        pyxel.rect(0, 0, 160, 120, self.backgroundColor)
        
        pyxel.rect(self.rect_x, self.rect_y, 248, 248, self.rect_color)
        
        pyxel.rect(self.rect_xx, self.rect_yy, 248, 248, 7)
        
        pyxel.rect(-9,0,10,120,7)
        pyxel.rect(159,0,10,120,7)
        pyxel.rect(0,-9,160,10,7)
        pyxel.rect(0,119,160,10,7)

App()