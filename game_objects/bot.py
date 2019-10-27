''' Module containing Bot class. '''

import consts


class Bot:
    ''' Class containing methods and variables related to the game bot. '''
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def update_paddle_position(self, ball, paddle):
        ''' Updates paddle position according to current position of the
            ball and bot's difficulty. '''
        if self.difficulty == 1:
            if not ball.curved:
                movement_start = consts.SCREEN_WIDTH_THREE_QUARTERS
            else:
                movement_start = consts.SCREEN_WIDTH_ONE_QUARTER
        elif self.difficulty == 2:
            movement_start = consts.SCREEN_WIDTH_HALF
        else:
            if not ball.curved:
                movement_start = consts.SCREEN_WIDTH_HALF
            else:
                movement_start = consts.SCREEN_WIDTH_TWO_THIRDS

        if ball.x <= movement_start or ball.x_direction_right is False:
            if paddle.y + consts.PADDLE_HALF < consts.SCREEN_HEIGHT_HALF:
                paddle.y += consts.PADDLE_SPEED
            elif paddle.y + consts.PADDLE_HALF > consts.SCREEN_HEIGHT_HALF:
                paddle.y -= consts.PADDLE_SPEED
        else:
            if ball.y <= paddle.y + consts.PADDLE_HALF:
                paddle.y -= consts.PADDLE_SPEED
            elif ball.y >= paddle.y + consts.PADDLE_HALF:
                paddle.y += consts.PADDLE_SPEED
