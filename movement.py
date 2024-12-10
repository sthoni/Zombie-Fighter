import pyxel


def movementP1(xPos):
    if pyxel.btn(pyxel.KEY_D):
        xPos += 20

    elif pyxel.btn(pyxel.KEY_A):
        xPos -= 20

    return xPos

def jump(yPos):
    jumpVelocity = 0


    if pyxel.btn(pyxel.KEY_W):
        yPos -= jumpVelocity
    return yPos