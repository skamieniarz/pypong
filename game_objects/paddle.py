''' Module containing Paddle class. '''

import consts
import pyxel


class Paddle:
    ''' Class containing methods and variables related to the paddle. '''
    def __init__(self, player):
        self.x = consts.BIG_MARGIN if player == 1 else (consts.SCREEN_WIDTH -
                                                        consts.BIG_MARGIN)
        self.y = consts.SCREEN_HEIGHT_HALF - consts.PADDLE_HALF
        self.player = player
        self.score = 0

    def draw(self):
        ''' Draws a paddle. '''
        if self.player == 1:
            pyxel.rectb(self.x, self.y, consts.PADDLE_WIDTH,
                        consts.PADDLE_LENGTH, consts.BLACK)
            pyxel.line(self.x + 1, self.y + 1, self.x + 1,
                       self.y + consts.PADDLE_LENGTH - 2, consts.RED)
        else:
            pyxel.rectb(self.x, self.y, consts.PADDLE_WIDTH,
                        consts.PADDLE_LENGTH, consts.BLACK)
            pyxel.line(self.x, self.y + 1, self.x,
                       self.y + consts.PADDLE_LENGTH - 2, consts.BLUE)

    def update_position(self):
        ''' Updates paddle's position according to pressed arrow key. '''
        screen_top = self.y < 0
        screen_bottom = self.y > consts.SCREEN_HEIGHT - consts.PADDLE_LENGTH
        if self.player == 1:
            if (pyxel.btn(pyxel.KEY_W)
                    or pyxel.btn(pyxel.GAMEPAD_1_UP)) and not screen_top:
                self.y -= consts.PADDLE_SPEED
            if (pyxel.btn(pyxel.KEY_S)
                    or pyxel.btn(pyxel.GAMEPAD_1_DOWN)) and not screen_bottom:
                self.y += consts.PADDLE_SPEED
        elif self.player == 2:
            if (pyxel.btn(pyxel.KEY_UP)
                    or pyxel.btn(pyxel.GAMEPAD_2_UP)) and not screen_top:
                self.y -= consts.PADDLE_SPEED
            if (pyxel.btn(pyxel.KEY_DOWN)
                    or pyxel.btn(pyxel.GAMEPAD_2_DOWN)) and not screen_bottom:
                self.y += consts.PADDLE_SPEED
