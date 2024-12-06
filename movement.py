import pyxel


def movementP1(xPos):
    if pyxel.btn(pyxel.KEY_D):
        print(xPos)
        xPos += 20
    return xPos
