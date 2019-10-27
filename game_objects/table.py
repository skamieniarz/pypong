''' Module containing Table class. '''

import consts
import pyxel
from helpers import get_center_x_coordinate


class Table:
    ''' Class containing methods and variables related to game's table. '''
    def draw(self, middle_line=True):
        ''' Draws ping pong table. '''
        pyxel.cls(consts.DARK_GREY)
        pyxel.rect(consts.MEDIUM_MARGIN, consts.MEDIUM_MARGIN,
                   consts.SCREEN_WIDTH - consts.BIG_MARGIN,
                   consts.SCREEN_HEIGHT - consts.BIG_MARGIN, consts.DARK_GREEN)
        if middle_line:
            pyxel.line(consts.MEDIUM_MARGIN, consts.SCREEN_HEIGHT / 2,
                       consts.SCREEN_WIDTH - consts.MEDIUM_MARGIN - 1,
                       consts.SCREEN_HEIGHT / 2, consts.WHITE)
        pyxel.rectb(consts.MEDIUM_MARGIN, consts.MEDIUM_MARGIN,
                    consts.SCREEN_WIDTH - consts.BIG_MARGIN,
                    consts.SCREEN_HEIGHT - consts.BIG_MARGIN, consts.WHITE)
        pyxel.text(get_center_x_coordinate('PyPong'), 2, 'PyPong',
                   consts.WHITE)

    def draw_scores(self, score_one, score_two):
        ''' Draws scores next to the ping pong table. '''
        left_score_margin = 4 if len(str(score_one)) == 1 else 2
        right_score_margin = 7 if len(str(score_two)) == 1 else 9
        pyxel.text(left_score_margin, (consts.SCREEN_HEIGHT / 2) - 2,
                   str(score_one), consts.WHITE)
        pyxel.text(consts.SCREEN_WIDTH - right_score_margin,
                   (consts.SCREEN_HEIGHT / 2) - 2, str(score_two),
                   consts.WHITE)
