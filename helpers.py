''' Module containing helper methods. '''

import consts


def get_center_x_coordinate(text):
    ''' Helper method that returns X coordinate for given text to be
        displayed in the center of the screen. '''
    return consts.SCREEN_WIDTH_HALF - (((len(text) * 4) - 1) / 2)


def get_center_y_coordinate(texts):
    ''' Helper method that returns Y coordinate for given list of texts
        to be displayed in the center of the screen. '''
    return consts.SCREEN_HEIGHT_HALF - ((
        (len(texts) * 2) - 1) / 2) - (round(len(texts) / 2) * 5)
