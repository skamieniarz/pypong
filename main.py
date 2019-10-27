'''
PyPong - a slightly modified clone of the classic Pong game implemented with
pyxel (https://github.com/kitao/pyxel).

Controls:
    W and S to move the first paddle up and down,
    ↑ and ↓ arrow controls to move the second paddle up and down,
    Q or P to pause the game,
    ENTER to choose option in menus.

Created by @skamieniarz (https://github.com/skamieniarz) in 2019.
'''

import pyxel
import consts
from game_objects.paddle import Paddle
from game_objects.menus import Menus, Controls, Win
from game_objects.ball import Ball
from game_objects.bot import Bot
from game_objects.table import Table
from time import time


class PyPong:
    ''' Main game class. '''
    def __init__(self):
        pyxel.init(consts.SCREEN_WIDTH,
                   consts.SCREEN_HEIGHT,
                   caption='PyPong',
                   scale=consts.SCALE)
        self.state = 'start'
        self.single_player = True
        self.table = Table()
        self.start_menu = Menus(consts.START_SCREEN)
        self.controls_menu = Controls(consts.CONTROLS_SCREEN_OPTIONS)
        self.bot_menu = Menus(consts.BOT_SCREEN_OPTIONS)
        self.pause_menu = Menus(consts.PAUSE_SCREEN_OPTIONS)
        self.win_screen = Win(consts.WIN_SCREEN)
        self.first_paddle = Paddle(player=1)
        self.second_paddle = Paddle(player=2)
        self.ball = Ball(x_direction_right=True)
        self.score_time = 0
        self.winner = None
        pyxel.run(self.update, self.draw)

    def reset(self):
        ''' Method resets the game. '''
        self.state = 'start'
        self.first_paddle = Paddle(player=1)
        self.second_paddle = Paddle(player=2)
        self.ball = Ball(x_direction_right=True)

    def update(self):
        ''' Main update function. '''

        menu_entrance_time = 0
        if self.state == 'start':
            selected_option = self.start_menu.update_selected_option()
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 0:
                self.single_player = True
                menu_entrance_time = time()
                self.state = 'bot'
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 1:
                self.single_player = False
                self.state = 'game'
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 2:
                menu_entrance_time = time()
                self.state = 'controls'
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 3:
                pyxel.quit()

        if self.state == 'controls' and time() - menu_entrance_time >= 1:
            selected_option = self.controls_menu.update_selected_option()
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 0:
                self.state = 'start'

        if self.state == 'bot' and time() - menu_entrance_time >= 1:
            selected_option = self.bot_menu.update_selected_option()
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 0:
                self.bot = Bot(1)
                self.state = 'game'
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 1:
                self.bot = Bot(2)
                self.state = 'game'
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 2:
                self.bot = Bot(3)
                self.state = 'game'
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 3:
                self.state = 'start'

        if self.state == 'game':
            self.ball.update_position()
            self.ball.edge_bounce()
            if not self.ball.x_direction_right:
                self.ball.paddle_bounce(self.first_paddle)
            if self.ball.x_direction_right:
                self.ball.paddle_bounce(self.second_paddle)
            self.first_paddle.update_position()
            if self.single_player:
                self.bot.update_paddle_position(self.ball, self.second_paddle)
            else:
                self.second_paddle.update_position()
            self.score_time = self.ball.score_event(self)
            self.winner = self.check_scores()
            if pyxel.btnp(pyxel.KEY_P) or pyxel.btnp(pyxel.KEY_Q):
                menu_entrance_time = time()
                self.state = 'pause'

        if self.state == 'score':
            self.ball.edge_bounce()
            self.first_paddle.update_position()
            if self.single_player:
                self.bot.update_paddle_position(self.ball, self.second_paddle)
            else:
                self.second_paddle.update_position()
            if time() - self.score_time >= 1:
                self.state = 'game'

        if self.state == 'pause':
            selected_option = self.pause_menu.update_selected_option()
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 0:
                self.state = 'game'
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 1:
                self.reset()

        if self.state == 'win':
            selected_option = self.win_screen.update_selected_option()
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 0:
                self.reset()
            if pyxel.btnp(pyxel.KEY_ENTER) and selected_option == 1:
                pyxel.quit()

    def draw(self):
        ''' Main method that draws game's objects. '''
        if self.state in consts.MENU_SCREENS:
            self.table.draw(middle_line=False)

        if self.state in ['start']:
            self.start_menu.draw()

        if self.state == 'controls':
            self.controls_menu.draw()
            self.controls_menu.display()

        if self.state == 'bot':
            self.bot_menu.draw()

        if self.state == 'pause':
            self.pause_menu.draw()

        if self.state in ['game', 'score']:
            self.table.draw()
            self.table.draw_scores(self.first_paddle.score,
                                   self.second_paddle.score)
            self.first_paddle.draw()
            self.second_paddle.draw()
            self.ball.draw()

        if self.state == 'win':
            self.win_screen.draw()
            self.win_screen.display(self.winner)

    def check_scores(self):
        ''' Checks score of both players. Ends game when one of the players
            has 11 points and has an advantage of at least 2 points. Returns
            the winner. '''
        winner = None
        if self.first_paddle.score >= 11 and (
                self.first_paddle.score - self.second_paddle.score >= 2):
            self.state = 'win'
            winner = 'Player 1'
        if self.second_paddle.score >= 11 and (
                self.second_paddle.score - self.first_paddle.score >= 2):
            self.state = 'win'
            winner = 'Player 2'
        return winner


if __name__ == '__main__':
    PyPong()
