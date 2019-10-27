''' Module containing Paddle class. '''

import consts
import pyxel

from time import time
from math import isclose
from random import randint, getrandbits


class Ball:
    ''' Class containing methods and variables related to the ball. '''
    def __init__(self, x_direction_right):
        self.x = consts.BIG_MARGIN + (
            consts.BALL_RADIUS * 2
        ) if x_direction_right else consts.SCREEN_WIDTH - consts.BIG_MARGIN - (
            consts.BALL_RADIUS * 2) + 1
        self.y = randint(int(consts.SCREEN_HEIGHT_ONE_QUARTER),
                         int(consts.SCREEN_HEIGHT_THREE_QUARTERS))
        self.speed = consts.BALL_SPEED
        self.x_direction_right = x_direction_right
        self.y_direction_up = bool(getrandbits(1))
        self.curved = False

    def draw(self):
        ''' Draws a ball. '''
        pyxel.circ(self.x, self.y, consts.BALL_RADIUS, consts.ORANGE)

    def update_position(self):
        ''' Updates ball's position according to current direction. '''

        extra_speed = 0 if self.curved else 1

        if self.x_direction_right and self.y_direction_up:
            self.x += self.speed + extra_speed
            self.y -= self.speed - extra_speed

        elif not self.x_direction_right and self.y_direction_up:
            self.x -= self.speed + extra_speed
            self.y -= self.speed - extra_speed

        elif self.x_direction_right and not self.y_direction_up:
            self.x += self.speed + extra_speed
            self.y += self.speed - extra_speed

        else:
            self.x -= self.speed + extra_speed
            self.y += self.speed - extra_speed

    def paddle_bounce(self, paddle):
        ''' Changes ball's direction and curve when bouncing off the
            paddle. '''
        paddle_edge = paddle.x + 1 if paddle.player == 1 else paddle.x
        if isclose(self.x, paddle_edge, abs_tol=consts.BALL_RADIUS):
            if (self.y + consts.BALL_RADIUS >=
                    paddle.y) and (self.y - consts.BALL_RADIUS <=
                                   paddle.y + consts.PADDLE_LENGTH):
                self.x_direction_right = not self.x_direction_right
                if (self.y + consts.BALL_RADIUS >
                        paddle.y + consts.PADDLE_LENGTH -
                        consts.PADDLE_TIP) or (self.y - consts.BALL_RADIUS <
                                               paddle.y + consts.PADDLE_TIP):
                    self.curved = True
                else:
                    self.curved = False

    def edge_bounce(self):
        ''' Changes ball's direction when bouncing off the table's edge. '''
        if self.y - consts.BALL_RADIUS <= consts.MEDIUM_MARGIN:
            self.y_direction_up = not self.y_direction_up
        elif self.y + consts.BALL_RADIUS >= (consts.SCREEN_HEIGHT -
                                             consts.MEDIUM_MARGIN):
            self.y_direction_up = not self.y_direction_up

    def score_event(self, game):
        ''' Increments paddle's score when ball is out of the table on the
            opponent's side and repositions the ball. Returns time of the
            score. '''
        score_time = 0
        if self.x >= consts.SCREEN_WIDTH or self.x <= 0:
            if self.x >= consts.SCREEN_WIDTH:
                game.first_paddle.score += 1
                game.ball = Ball(x_direction_right=False)
            else:
                game.second_paddle.score += 1
                game.ball = Ball(x_direction_right=True)
            game.state = 'score'
            score_time = time()
        return score_time
