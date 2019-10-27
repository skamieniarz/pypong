''' Module containing Menus related classes. '''

import consts
import pyxel

from helpers import get_center_x_coordinate, get_center_y_coordinate


class Menus:
    ''' Class containing methods and variables related to game's menus like
        start or pause menus. '''
    def __init__(self, options):
        self.options = options
        self.selected_option = 0
        self.options_amount = len(self.options)

    def draw(self):
        ''' Draws menu options and currently selected item. '''
        longest_text = max(self.options, key=len)
        center_x_cord = get_center_x_coordinate(longest_text)
        center_y_cord = get_center_y_coordinate(self.options)
        for index, text in enumerate(self.options):
            pyxel.text(center_x_cord,
                       center_y_cord + index * consts.MEDIUM_MARGIN, text,
                       consts.WHITE)
        pyxel.circ(center_x_cord - 6,
                   ((center_y_cord + consts.BALL_RADIUS) +
                    (consts.MEDIUM_MARGIN * self.selected_option)),
                   consts.BALL_RADIUS, consts.ORANGE)

    def update_selected_option(self):
        ''' Updates currently selected options item and returns it. '''
        if pyxel.btnp(pyxel.KEY_UP) and self.selected_option > 0:
            self.selected_option -= 1
        if pyxel.btnp(pyxel.KEY_DOWN) and self.selected_option < (
                len(self.options) - 1):
            self.selected_option += 1
        return self.selected_option


class Controls(Menus):
    def display(self):
        ''' Displays controls info. '''
        longest_text = max(consts.CONTROLS, key=len)
        center_x_cord = get_center_x_coordinate(longest_text)
        for index, text in enumerate(consts.CONTROLS):
            pyxel.text(center_x_cord,
                       consts.BIG_MARGIN + index * consts.MEDIUM_MARGIN, text,
                       consts.WHITE)


class Win(Menus):
    def display(self, winner):
        ''' Displays the winner. '''
        text = f'The winner is: {winner}'
        center_x_cord = get_center_x_coordinate(text)
        pyxel.text(center_x_cord, consts.BIG_MARGIN, text, consts.WHITE)
