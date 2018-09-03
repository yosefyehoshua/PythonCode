#############################################################################
# FILE : asteroids.py
# WRITER : Yoav Galtzur, yoav.galtzur, 203372511
# WRITER : Yosef Yehoshua, yosef12345, 302818513
# EXERCISE : intro2cs ex9 2015-2016
# DESCRIPTION : A class managing the game 'Asteroids'
#############################################################################

#############################################################################
# IMPORTS
#############################################################################
from screen import Screen
from ship import Ship
from asteroid import Asteroid
import sys
import copy
from torpedo import Torpedo
#############################################################################
# CONSTANTS
#############################################################################
DEFAULT_ASTEROIDS_NUM = 5
ASTEROID_START_SIZE = 3
TITLE = "Shit Happens"
DEAD_MSG = "You're Dead"
VICTORY_TITLE = "I can't believe it!"
VICTORY_MSG = "You Won!"
LOSE_LIFE_MSG = "You've lost one life..."
LEAVE_TITLE = "I wanna see you out that door"
LEAVE_MSG = "Baby, bye, bye, bye"
ANGLE = 7
MAX_TORPEDO = 15
MIN_SPLIT_SIZE = 1
AST_SIZE_3_SCORE = 20
AST_SIZE_2_SCORE = 50
AST_SIZE_1_SCORE = 100
DECREASE_AST_SIZE = 1
BIG_AST_SIZE = 3
MID_AST_SIZE = 2
SMALL_AST_SIZE = 1


#############################################################################
# GameRunner CLASS
#############################################################################
class GameRunner:
    """
    A class managing the game 'Asteroids'
    """

    def __init__(self, asteroids_amnt):
        """
        Initializing a new game of 'Asteroids'
        :param asteroids_amnt: The number of asteroids to begin with
        """
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.ship = Ship(self.screen_max_x, self.screen_max_y,
                         self.screen_min_x, self.screen_min_y)
        self.asteroids_amnt = asteroids_amnt
        self.asteroids_list = []
        self.create_asteroids()
        self.__torpedoes_list = []
        self.__score = 0

    def create_asteroids(self):
        """
        creating the no. of asteroids given, providing them with ID
        and assigning them to a designated dictionary
        """
        for count in range(self.asteroids_amnt):
            # create new asteroid and assign it to the dictionary
            new_ast = Asteroid(ASTEROID_START_SIZE, self.screen_max_x,
                               self.screen_max_y, self.screen_min_x,
                               self.screen_min_y)
            self.asteroids_list.append(new_ast)
            self._screen.register_asteroid(new_ast, new_ast.get_size())

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def move_ship(self):
        """
        Checks if the ship's angle is changed and if ship was accelerated
        and moves the ships accordingly
        """
        if self._screen.is_left_pressed():  # Angle should increase
            self.ship.set_angle(ANGLE)
        elif self._screen.is_right_pressed():  # Angle should decrease
            self.ship.set_angle(-ANGLE)
        if self._screen.is_up_pressed():  # Ship should accelerate
            self.ship.accelerate()
        self.ship.set_position()  # Change position according to changes

    def create_torpedo(self):
        """
        Creates a new torpedo if no. of torpedoes is smaller than max value
        """
        if len(self.__torpedoes_list) < MAX_TORPEDO:
            new_torpedo = Torpedo(self.ship.get_angle(), self.ship.get_pos_x(),
                                  self.ship.get_pos_y(),
                                  self.ship.get_speed_x(),
                                  self.ship.get_speed_y(), self.screen_max_x,
                                  self.screen_max_y, self.screen_min_x,
                                  self.screen_min_y)
            self.__torpedoes_list.append(new_torpedo)
            self._screen.register_torpedo(new_torpedo)

    def move_torpedo(self):
        """
        Checks if torpedo life span has reached and deletes it,
        otherwise, sets the torpedo's new position and prints it to the screen
        :return:
        """
        for torpedo in copy.copy(self.__torpedoes_list):
            if torpedo.is_dead():  # Life span reached
                self.__torpedoes_list.remove(torpedo)
                self._screen.unregister_torpedo(torpedo)

        for torpedo in self.__torpedoes_list:
            torpedo.lose_life()
            torpedo.set_position()
            self._screen.draw_torpedo(torpedo, torpedo.get_pos_x(),
                                      torpedo.get_pos_y(), torpedo.get_angle())

    def create_new_asteroid(self, new_size, torpedo, asteroid,
                            reverse=False):
        """
        Creates two sub_asteroids of a given asteroid that was hit by
        a torpedo
        :param new_size: the size of the new sub-asteroids
        :param torpedo: the torpedo that damaged the asteroid
        :param asteroid: the old asteroid that was hit by a torpedo
        :param reverse: Boolean value, checking if the new generated direction
        should be reversed
        """
        new_ast = Asteroid(new_size, self.screen_max_x, self.screen_max_y,
                           self.screen_min_x, self.screen_min_y)
        self.asteroids_list.append(new_ast)
        # Assigning new speed according to the asteroid's and torpedo's
        # old speed
        new_ast.gen_speed_x(torpedo.get_speed_x(), asteroid.get_speed_x())
        new_ast.gen_speed_y(torpedo.get_speed_y(), asteroid.get_speed_y())
        # Assigning the position of the dead asteroid to the sub-asteroid
        new_ast.force_pos_x(asteroid.get_pos_x())
        new_ast.force_pos_y(asteroid.get_pos_y())
        if reverse:
            new_ast.reverse_direction()
        self._screen.register_asteroid(new_ast, new_size)
        self._screen.draw_asteroid(new_ast, new_ast.get_pos_x(),
                                   new_ast.get_pos_y())

    def handle_intersection(self, torpedo, asteroid):
        """
        Deleting the intersected torpedo and asteroid, initiating the creation
        of sub-asteroids if needed. Also, updating score
        :param torpedo: the torpedo involved in the intersection
        :param asteroid: the asteroid involved in the intersection
        """
        # Deleting the intersected asteroid
        self.__torpedoes_list.remove(torpedo)
        self._screen.unregister_torpedo(torpedo)
        # Deleting the intersected asteroid
        self._screen.unregister_asteroid(asteroid)
        self.asteroids_list.remove(asteroid)
        self.add_score(asteroid.get_size())
        if asteroid.get_size() > MIN_SPLIT_SIZE:
            # Defining the size of the new sub-asteroids
            new_size = asteroid.get_size() - DECREASE_AST_SIZE
            # Create the first sub-asteroid
            self.create_new_asteroid(new_size, torpedo, asteroid)
            # Create the second sub-asteroid
            self.create_new_asteroid(new_size, torpedo, asteroid, True)

    def ship_intersection(self, asteroid):
        """
        Checking for ship intersections with asteroids. Updating the ship's
        lives and ending game if lives ended
        :param asteroid: The asteroid checked for intersection
        :return:
        """
        if asteroid.has_intersection(self.ship):
            self.ship.lose_life()
            self._screen.unregister_asteroid(asteroid)
            self.asteroids_list.remove(asteroid)
            if self.ship.is_dead():
                self._screen.show_message(TITLE, DEAD_MSG)
                self._screen.end_game()
                sys.exit()
            else:
                self._screen.show_message(TITLE, LOSE_LIFE_MSG)
                self._screen.remove_life()

    def add_score(self, size):
        """
        Updating the score according to the size of the danaged asteroid
        :param size: The size of the damaged asteroid
        """
        if size == BIG_AST_SIZE:
            self.__score += AST_SIZE_3_SCORE
        if size == MID_AST_SIZE:
            self.__score += AST_SIZE_2_SCORE
        if size == SMALL_AST_SIZE:
            self.__score += AST_SIZE_1_SCORE

    def check_ending(self):
        """
        Check if one of two ending conditions has reached:
        1. The player pressed 'q' or 'Quit button'
        2. All asteroids are gone - winning condition
        """

        if len(self.asteroids_list) == 0:
            self._screen.show_message(VICTORY_TITLE, VICTORY_MSG)
            self._screen.end_game()
            sys.exit()
        # Checking if 'q' or 'Quit' button was pressed
        elif self._screen.should_end():
            self._screen.show_message(LEAVE_TITLE, LEAVE_MSG)
            self._screen.end_game()
            sys.exit()

    def _game_loop(self):
        """
        Manages a single round of the game 'Asteroids',
        """

        self.check_ending()
        # Moving and drawing the ship
        self.move_ship()
        self._screen.draw_ship(self.ship.get_pos_x(), self.ship.get_pos_y(),
                               self.ship.get_angle())
        # If the player wants to shoot a torpedo
        if self._screen.is_space_pressed():
            self.create_torpedo()
        # Moving the other objects in the game, checking for intersections
        # and updating status accordingly
        self.move_torpedo()
        for asteroid in copy.copy(list(self.asteroids_list)):
            asteroid.set_position()
            self._screen.draw_asteroid(asteroid, asteroid.get_pos_x(),
                                       asteroid.get_pos_y())
            for torpedo in copy.copy(self.__torpedoes_list):
                if asteroid.has_intersection(torpedo):
                    self.handle_intersection(torpedo, asteroid)
                    break  # Only 1 torpedo can intersect with an asteroid
            else:  # No intersections were made
                self.ship_intersection(asteroid)
        self._screen.set_score(self.__score)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(3)
