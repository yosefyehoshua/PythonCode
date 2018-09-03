#############################################################################
# FILE : torpedo.py
# WRITER : Yoav Galtzur, yoav.galtzur, 203372511
# WRITER : Yosef Yehoshua, yosef12345, 302818513
# EXERCISE : intro2cs ex9 2015-2016
# DESCRIPTION : A class representing a torpedo in a game 'Asteroids'
#############################################################################

#############################################################################
# IMPORTS
#############################################################################
from asteroids_helper import Helper
import math

#############################################################################
# CONSTANTS
#############################################################################
TORPEDO_LIFE_SPAN = 200
TORPEDO_RADIUS = 4
SPEED_FACTOR = 2


#############################################################################
# Torpedo CLASS
#############################################################################

class Torpedo:
    """
    A class representing a ship in the game 'Asteroids'
    """

    def __init__(self, angle, pos_x, pos_y, speed_x, speed_y, SCREEN_MAX_X,
                 SCREEN_MAX_Y, SCREEN_MIN_X, SCREEN_MIN_Y):
        """
        :param angle: The given angle of the torpedo
        :param pos_x: The given position of the torpedo on the X axis
        :param pos_y: The given position of the torpedo on the Y axis
        :param speed_x: The given speed of the torpedo on the X axis
        :param speed_y: The given speed of the torpedo on the Y axis
        :param SCREEN_MAX_X: max X coor of the screen
        :param SCREEN_MAX_Y: max Y coor of the screen
        :param SCREEN_MIN_X: min X coor of the screen
        :param SCREEN_MIN_Y: min Y coor of the screen
        """
        self.__help = Helper()  # an object of the Helper class
        self.__angle = angle
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__radius = TORPEDO_RADIUS
        self.__life_span = TORPEDO_LIFE_SPAN
        self.screen_max_x = SCREEN_MAX_X
        self.screen_max_y = SCREEN_MAX_Y
        self.screen_min_x = SCREEN_MIN_X
        self.screen_min_y = SCREEN_MIN_Y
        self.length_x_axis = SCREEN_MAX_X - SCREEN_MIN_X
        self.length_y_axis = SCREEN_MAX_Y - SCREEN_MIN_Y
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.set_speed()

    def get_pos_x(self):
        """
        :return: position of the torpedo on the X (horizontal) axis
        """
        return self.__pos_x

    def get_pos_y(self):
        """
        :return: position of the torpedo on the Y (vertical) axis
        """
        return self.__pos_y

    def get_lives(self):
        """
        :return: torpedo's remaining life span
        """
        return self.__life_span

    def get_angle(self):
        """
        :return: angle of the torpedo
        """
        return self.__angle

    def get_radius(self):
        """
        :return: radius of the torpedo
        """
        return self.__radius

    def get_speed_x(self):
        """
        :return: The torpedo's speed on the X (horizontal) axis
        """
        return self.__speed_x

    def get_speed_y(self):
        """
        :return: The torpedo's speed on the Y (vertical) axis
        """
        return self.__speed_y

    def set_position(self):
        """
        Sets new position to the torpedo, according to its speed
        and former pos
        """
        self.__pos_x = self.__help.set_postion_on_axis(self.__pos_x,
                                                       self.__speed_x,
                                                       self.screen_min_x,
                                                       self.length_x_axis)
        self.__pos_y = self.__help.set_postion_on_axis(self.__pos_y,
                                                       self.__speed_y,
                                                       self.screen_min_y,
                                                       self.length_y_axis)

    def set_speed(self):
        """
        Sets the torpedo speed when created (speed remains the same
        throughout the game)
        """
        angle = self.__help.angle_to_radians(self.__angle)
        self.__speed_x += SPEED_FACTOR * math.cos(angle)
        self.__speed_y += SPEED_FACTOR * math.sin(angle)

    def lose_life(self):
        """
        Decreasing 1 from the torpedo's remaining life span
        """
        self.__life_span -= 1

    def is_dead(self):
        """
        :return: True if torpedo's life span have reached, False otherwise
        """
        if self.__life_span == 0:
            return True
        else:
            return False
