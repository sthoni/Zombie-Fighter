import pyxel
import movement
import time

class App:
    def __init__(self):
        pyxel.init(180, 100)
        
        # Players
        self.rect_x1, self.rect_x2 = 60, 120
        self.rect_y1, self.rect_y2 = -100, -100

        self.hp1, self.hp2 = 1000, 1000  # 1000, 1000

        self.velocity_p1, self.velocity_p2 = 0, 0

        self.p1_indikator, self.p2_indikator = 3, 3

        self.p1IsPunching, self.p2IsPunching = False, False
        self.p1LastPunchTime, self.p2LastPunchTime = time.time(), time.time()  # Zeit vom letzten Schlag

        self.p1_last_jump_time, self.p2_last_jump_time = time.time(), time.time()

        self.p1richtung,self.p2richtung = "links", "rechts"

        self.state_player_1, self.state_player_2 = str, str

        self.block_indicator_p1 = 0
        self.block_sound_played_p1 = False

        self.block_indicator_p2 = 0
        self.block_sound_played_p2 = False
        

        # General
        self.gravity = 0.75

        self.speed = 3
        self.speed_block = self.speed // 2

        self.backgroundColor = 0
       
        pyxel.load("res.pyxres")
        self.musik_started = False

        self.game_over_music = False

        self.state = "Menu"

        #Main Menu
        self.button_main_menu = 1
        self.time_last_button_switch = time.time()

        #Game Over Menu
        self.button_game_over = 1
        self.time_last_button_switch_game_over = time.time()
        self.press_cooldown_game_over = 5

        self.block_cooldown_p1 = time.time() -4
        self.block_cooldown_p2 = time.time() -4

        pyxel.run(self.update, self.draw)


    def update(self):
        if self.state == "Menu":
            self.update_menu()
        elif self.state == "Controls":
            self.update_controls()
        elif self.state == "Game":
            self.update_game()
        elif self.state == "Game Over":
            self.update_game_over()



    def update_menu(self):

        if pyxel.btn(pyxel.KEY_DOWN) and time.time() - self.time_last_button_switch >= 0.1:
            self.button_main_menu -= 1
            self.time_last_button_switch = time.time()
            pyxel.play(1, 55)
        if pyxel.btn(pyxel.KEY_UP) and time.time() - self.time_last_button_switch >= 0.1:
            self.button_main_menu += 1
            self.time_last_button_switch = time.time()
            pyxel.play(1, 55)

        if self.button_main_menu % 2 == 0 and pyxel.btn(pyxel.KEY_RETURN) and time.time() - self.press_cooldown_game_over >= 1:
            self.state = "Game"
            pyxel.play(2, 53)
        if self.button_main_menu % 2 == 1 and pyxel.btn(pyxel.KEY_RETURN) and time.time() - self.press_cooldown_game_over >= 1:
            self.state = "Controls"
            pyxel.play(2, 53)

    def update_controls(self):

        if pyxel.btn(pyxel.KEY_LEFT):
            self.state = "Menu"
            print("Controls")
            pyxel.play(2, 53)
      

    def update_game(self):

        if self.hp1 <= 0 or self.hp2 <= 0:
            self.state = "Game Over" 

        # Gravitation
        self.rect_y1, self.velocity_p1 = movement.gravitation(self.rect_y1, self.gravity, self.velocity_p1)

        self.rect_y2, self.velocity_p2 = movement.gravitation(self.rect_y2, self.gravity, self.velocity_p2)

        # Play Music
        #if self.musik_started == False:
        #    pyxel.playm(2, loop = True)
        #    self.musik_started = True


        # Movement
        self.rect_x1, self.p1richtung = movement.movementP1(self.rect_x1, self.p1richtung, self.state_player_1, 
                                                            self.speed, self.speed_block)

        self.rect_x2, self.p2richtung = movement.movementP2(self.rect_x2, self.p2richtung, self.state_player_2, 
                                                            self.speed, self.speed_block)

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
        if pyxel.btnr(pyxel.KEY_CTRL) and time.time() - self.block_cooldown_p1 >= 4:
            self.block_cooldown_p1 = time.time()
        if pyxel.btn(pyxel.KEY_CTRL) and time.time() - self.block_cooldown_p1 >= 4:
            self.state_player_1 = "blocking"
        else:
            self.state_player_1 = "normal"

        
        if time.time() - self.block_cooldown_p1 >= 4:
            self.block_indicator_p1 = 3
            if self.block_sound_played_p1 == 8:
                pyxel.play(3,57)
            self.block_sound_played_p1 = 3
        else:
            self.block_indicator_p1 = 8
            self.block_sound_played_p1 = 8



        if pyxel.btnr(pyxel.KEY_KP_5) and time.time() - self.block_cooldown_p2 >= 4:
            self.block_cooldown_p2 = time.time()
        if pyxel.btn(pyxel.KEY_KP_5) and time.time() - self.block_cooldown_p2 >= 4:
            self.state_player_2 = "blocking"
        else:
            self.state_player_2 = "normal"

        if time.time() - self.block_cooldown_p2 >= 4:
            self.block_indicator_p2 = 3
            if self.block_sound_played_p2 == 8:
                pyxel.play(3,58)
            self.block_sound_played_p2 =3
        else:
            self.block_indicator_p2 = 8
            self.block_sound_played_p2 = 8

        
        
        # Schlag
        self.p1IsPunching, self.p1LastPunchTime, self.hp2, self =  movement.punch_p1(self, self.p1IsPunching, self.p1LastPunchTime, self.rect_x2, self.rect_x1, self.hp2)

        self.p2IsPunching, self.p2LastPunchTime, self.hp1 =  movement.punch_p2(self, self.p2IsPunching, self.p2LastPunchTime, self.rect_x1, self.rect_x2, self.hp1)
        

        if time.time() - self.p1LastPunchTime >= 0.5:
            self.p1_indikator = 3
        else:
            self.p1_indikator = 8


        if time.time() - self.p2LastPunchTime >= 0.5:
            self.p2_indikator = 3
        else:
            self.p2_indikator = 8
        

    def update_game_over(self):

        if pyxel.btn(pyxel.KEY_DOWN) and time.time() - self.time_last_button_switch_game_over >= 0.1:
            self.button_game_over -= 1
            self.time_last_button_switch_game_over = time.time()
            pyxel.play(1, 55)

        if pyxel.btn(pyxel.KEY_UP) and time.time() - self.time_last_button_switch_game_over >= 0.1:
            self.button_game_over += 1
            self.time_last_button_switch_game_over = time.time()
            pyxel.play(1, 55)

        if self.button_game_over % 2 == 0 and pyxel.btn(pyxel.KEY_RETURN):
            
            self.state = "Game"
            pyxel.play(2, 53)

            self.hp1, self.hp2 = 1000, 1000
            self.musik_started = False
            self.game_over_music = False

        if self.button_game_over % 2 == 1 and pyxel.btn(pyxel.KEY_RETURN):

            self.state = "Menu"
            self.press_cooldown_game_over = time.time()
            pyxel.play(2, 53)


            self.hp1, self.hp2 = 1000, 1000
            self.musik_started = False
            self.game_over_music = False



    def draw(self):
        if self.state == "Game":
            self.draw_main_game()

        elif self.state == "Game Over":
            self.draw_game_over()

        elif self.state == "Menu":
            self.draw_menu()

        elif self.state == "Controls":
            self.draw_controls()


    def draw_main_game(self):
        pyxel.cls(0)

        pyxel.blt(0,0,2, 0, 0, 180, 100)

        #Spieler 1

        #pyxel.rect(self.rect_x1, self.rect_y1, 32, 32, 2)

        #if self.p1richtung == "rechts":
        #    pyxel.rect(self.rect_x1 + 30, self.rect_y1 + 4, 2, 2 ,0)

        #if self.p1richtung == "links":
        #    pyxel.rect(self.rect_x1, self.rect_y1 + 4, 2, 2 ,0)

        pyxel.blt(self.rect_x1, self.rect_y1, 0, 0, 0, 32, 32, 0)


        #Spieler 2

        #pyxel.rect(self.rect_x2, self.rect_y2, 32, 32, 1)

        #if self.p2richtung == "rechts":
        #    pyxel.rect(self.rect_x2 + 30, self.rect_y2 + 4, 2,2 ,0)

        #if self.p2richtung == "links":
        #    pyxel.rect(self.rect_x2 , self.rect_y2 + 4, 2,2 ,0)

        pyxel.blt(self.rect_x2, self.rect_y2, 0, 67, 0, 32, 32, 0)

        # HP bar for Player 1
        pyxel.rect(12, 7, 1000 / 22, 5, 8)
        pyxel.rect(12, 7, self.hp1 / 22, 5, 3)
        pyxel.rectb(12, 6, 1000 / 22, 6, 0)

        # Cooldown indikator p1
        pyxel.rect(12, 20, 5,5, self.p1_indikator)
        pyxel.rect(20, 20, 5,5, self.block_indicator_p1)

        # HP bar for Player 2
        pyxel.rect(120, 7, 1000 / 22, 5, 8)
        pyxel.rect(120, 7, self.hp2 / 22, 5, 3)
        pyxel.rectb(120, 6, 1000 / 22, 6, 0)

        # Cooldown indikator p2
        pyxel.rect(120, 20, 5,5, self.p2_indikator)
        pyxel.rect(128, 20, 5,5, self.block_indicator_p2)

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


    def draw_game_over(self):
        pyxel.rect(0,0, 180, 100, 0)

        pyxel.text(70,5,"Game Over", 8)

        pyxel.text(63, 15 , "Player 2 wins" if self.hp1 <= 0 else "Player 1 wins", 8)

        pyxel.text(70, 50, "Play Again", 7)
        if self.button_game_over % 2 == 0:
            pyxel.rectb(67, 48, 45,10,7)


        pyxel.text(72, 70, "Main Menu", 7)
        if self.button_game_over % 2 == 1:
            pyxel.rectb(68, 68, 42,10,7)
        
        
        #Game over Musik nicht doppelt abspielen
        # (N) Logik gehört nicht in der draw Methode
        if not self.game_over_music:
            self.game_over_music = True
            pyxel.stop()
            pyxel.play(3,49)
            pyxel.playm(1, loop = False)
        

    def draw_menu(self):
        pyxel.rect(0,0,180,100,0)

        pyxel.text(65,30,"Street Fighter", 7)

        pyxel.text(85,50,"PLAY", 7)
        if self.button_main_menu % 2 == 0:
            pyxel.rectb(82,48,20,10, 7)

        pyxel.text(78,64,"Controls", 7)
        if self.button_main_menu % 2 != 0:
            pyxel.rectb(75,62,38,10, 7)


    def draw_controls(self):
        pyxel.rect(0,0,180,100,0)
        pyxel.text(35,90,"Press Left Arrow to escape", 7)

        pyxel.text(77,5,"Controls", 7)



        pyxel.text(5,20,"Movement Player 1: W A S D", 1)
        pyxel.text(5, 30, "Punch Player 1: SPACE", 1)
        pyxel.text(5, 40, "Block Player 1: STRG", 1)
        
        pyxel.text(5,55,"Movement Player 2: Arrow Keys", 2)
        pyxel.text(5, 65, "Punch Player 2: 0 (Numpad)", 2)
        pyxel.text(5, 75, "Block Player 2: 5 (Numpad)", 2)



App()