import pyxel
import random

def mov_animation(animation_timer, movement_frame, p_moving, p_state, p_hits, rect_x, rect_y, p_1_direction):
    animation_timer += 1

    if animation_timer % 4 == 0:
        if (animation_timer / 4) % 2:
            movement_frame = 0
        else:
            movement_frame = 1
    
    if p_moving and p_state == "normal" and not p_hits:
        if movement_frame == 0:
            pyxel.blt(rect_x - 3, rect_y, 0, 0, 200, 32, 32, 10) if p_1_direction == "right" else\
            pyxel.blt(rect_x, rect_y, 0, 67, 100, 32, 32, 10)
        else:
            pyxel.blt(rect_x, rect_y, 0, 67, 1, 32, 32, 10)  if p_1_direction == "right" else\
            pyxel.blt(rect_x, rect_y, 0, 34, 200, 32, 32, 10)

    elif not p_moving and p_state == "normal" and not p_hits: # idle frame
        pyxel.blt(rect_x, rect_y, 0, 67, 1, 32, 32, 10) if p_1_direction  == "right" else\
        pyxel.blt(rect_x, rect_y, 0, 67, 100, 32, 32, 10)

    return animation_timer, movement_frame


def block_animation(state_player, player_hits, player_direction, rect_x, rect_y):

    if state_player == "blocking" and not player_hits:
            pyxel.blt(rect_x, rect_y, 0, 100, 1, 32, 32, 10) if player_direction == "right" else\
            pyxel.blt(rect_x, rect_y, 0, 100, 100, 32, 32, 10)


def hit_animation(p_is_punching, p_hits, count_images_hit, count_hit_images, choose_animation, p_1_direction, rect_x, rect_y):
    if p_is_punching:
            p_hits = True
        
    if p_hits:
        count_images_hit += 1

    if p_hits and count_hit_images != 3:
        if count_hit_images == 1:
            choose_animation = random.randint(1, 2)
            print(choose_animation)

            pyxel.blt(rect_x + 4, rect_y, 0, 0 if choose_animation == 1 else 67, 67, 32, 32, 10) if p_1_direction == "right" else\
            pyxel.blt(rect_x - 7, rect_y, 0, 0 if choose_animation == 1 else 67, 167, 32, 32, 10)

        elif count_hit_images == 2:
            pyxel.blt(rect_x + 6, rect_y, 0, 34 if choose_animation == 1 else 100, 67, 32, 32, 10) if p_1_direction == "right" else\
            pyxel.blt(rect_x - 9, rect_y, 0, 34 if choose_animation == 1 else 100, 167, 32, 32, 10)

        if count_images_hit % 3 == 0:
            count_hit_images += 1
    else: 
        p_hits = False
        count_hit_images = 0

    return p_hits, count_images_hit, count_hit_images, choose_animation