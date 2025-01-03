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
        self.p1LastPunchTime = time.time()  # Zeit vom letzten Schlag

        self.p1_last_jump_time = time.time()

        self.p1richtung = "rechts"

        self.p1_indikator = 3

        self.state_player_1 = str

        # Player 2
        self.rect_x2 = 150
        self.rect_y2 = 10

        self.hp2 = 1000

        self.velocity_p2 = 0


        self.p2richtung = "links"

        self.p2_indikator = 3
        
        self.gravity = 0.75

        self.p2IsPunching = False
        self.p2LastPunchTime = time.time()  # Zeit vom letzten Schlag

        self.p2_last_jump_time = time.time()

        self.backgroundColor = 0
        

        self.new_hp_bar = 35

        self.state_player_2 = str


        pyxel.load("res.pyxres")  # Ressourcen-Datei laden
        pyxel.playm(0, loop= True)

        self.game_over_music = False

        pyxel.run(self.update, self.draw)


    def update(self):
        # Gravitation

        self.rect_y1, self.velocity_p1 = movement.gravitation(self.rect_y1, self.gravity, self.velocity_p1)

        self.rect_y2, self.velocity_p2 = movement.gravitation(self.rect_y2, self.gravity, self.velocity_p2)


        # Movement
        self.rect_x1, self.p1richtung = movement.movementP1(self.rect_x1, self.p1richtung)

        self.rect_x2, self.p2richtung = movement.movementP2(self.rect_x2, self.p2richtung)

        # Jump
        if 62 > self.rect_y1 > 55:
            self.rect_y1 = 59.5
        if 62 > self.rect_y2 > 55:
            self.rect_y2 = 59.5

        if pyxel.btn(pyxel.KEY_W):
            self.rect_y1, self.p1_last_jump_time = movement.jump(self.rect_y1, self.p1_last_jump_time)

        if pyxel.btn(pyxel.KEY_UP):
            self.rect_y2, self.p2_last_jump_time = movement.jump(self.rect_y2, self.p2_last_jump_time)

        # Block
        if pyxel.btn(pyxel.KEY_CTRL):
            self.state_player_1 = "blocking"
        else:
            self.state_player_1 = "normal"

        if pyxel.btn(pyxel.KEY_KP_5):
            self.state_player_2 = "blocking"
        else:
            self.state_player_2 = "normal"
        
        # Schlag
        if self.state_player_2 == "normal" and self.state_player_1 == "normal":
            self.p1IsPunching, self.p1LastPunchTime, self.hp2 =  movement.punch_p1(self.p1IsPunching, self.p1LastPunchTime, self.rect_x2, self.rect_x1, self.hp2)

        if self.state_player_1 == "normal" and self.state_player_2 == "normal":
            self.p2IsPunching, self.p2LastPunchTime, self.hp1 =  movement.punch_p2(self.p2IsPunching, self.p2LastPunchTime, self.rect_x1, self.rect_x2, self.hp1)
        

        if time.time() - self.p1LastPunchTime >= 0.5:
            self.p1_indikator = 3
        else:
            self.p1_indikator = 8


        if time.time() - self.p2LastPunchTime >= 0.5:
            self.p2_indikator = 3
        else:
            self.p2_indikator = 8

    def draw(self):
        pyxel.cls(0)
        
        #Spieler 1

        pyxel.rect(self.rect_x1, self.rect_y1, 32, 32, 2)

        if self.p1richtung == "rechts":
            pyxel.rect(self.rect_x1 +30, self.rect_y1 + 4, 2,2 ,0)

        if self.p1richtung == "links":
            pyxel.rect(self.rect_x1, self.rect_y1 + 4, 2,2 ,0)


        #Spieler 2

        pyxel.rect(self.rect_x2, self.rect_y2, 32, 32, 1)

        if self.p2richtung == "rechts":
            pyxel.rect(self.rect_x2 +30, self.rect_y2 + 4, 2,2 ,0)

        if self.p2richtung == "links":
            pyxel.rect(self.rect_x2 , self.rect_y2 + 4, 2,2 ,0)


        # HP bar for Player 1
        pyxel.rect(12, 7, 1000 / 22, 5, 8)
        pyxel.rect(12, 7, self.hp1 / 22, 5, 3)

        # Cooldown indikator p1
        pyxel.rect(12, 20, 5,5, self.p1_indikator)

        # HP bar for Player 2
        pyxel.rect(120, 7, 1000 / 22, 5, 8)
        pyxel.rect(120, 7, self.hp2 / 22, 5, 3)

        # Cooldown indikator p2
        pyxel.rect(120, 20, 5,5, self.p2_indikator)

        # Block indikator
        if self.state_player_1 == "blocking":
            pyxel.rect(self.rect_x1 + 9, self.rect_y1 + 9, 13, 13, 13)

        if self.state_player_2 == "blocking":
            pyxel.rect(self.rect_x2 + 9, self.rect_y2 + 9, 13, 13, 13)





        if self.p1IsPunching:
            pyxel.rect(self.rect_x1 + 40, self.rect_y1 + 5, 20, 20, 8)
            pyxel.rect(self.rect_x1 - 28, self.rect_y1 + 5, 20, 20, 8)

        if self.p2IsPunching:
            pyxel.rect(self.rect_x2 + 40, self.rect_y2 + 5, 20, 20, 8)
            pyxel.rect(self.rect_x2 - 28, self.rect_y2 + 5, 20, 20, 8)

        pyxel.rect(70,10, 16,16,10)
        pyxel.blt(70, 10, 0, 0, 0, 16, 16, 14)  

        if self.hp1 <= 0 or self.hp2 <= 0:
            pyxel.rect(0,0, 180, 100, 0)
            pyxel.text(70,30,"Game Over", 8)


            if self.hp1 <= 0:
                winner = "Player 2 wins"
            else:
                winner = "Player 1 wins"

            pyxel.text(65,50,winner, 8)
            
            

            if not self.game_over_music:
                self.game_over_music = True
                pyxel.stop()
                pyxel.playm(1, loop= False)
        
        

App()