############################################################
# Helper class
############################################################
import copy
import ship_helper


class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
     NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
     implementations are for you to carry out.
    """
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    NOT_MOVING = 0

    VERTICAL = (UP, DOWN)
    HORIZONTAL = (LEFT, RIGHT)

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)


############################################################
# Class definition
############################################################


class Ship:
    """
    A class representing a ship in Battleship game.
    A ship is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A ship sails on its vertical\horizontal axis back and
    forth until reaching the board's boarders and then changes its direction to
    the opposite (left <--> right, up <--> down).
    If a ship is hit in one of its coordinates, it ceases its movement in all
    future turns.
    A ship that had all her coordinates hit is considered terminated.
    """
    def __init__(self, pos, length, direction, board_size):
        """
        A constructor for a Ship object
        :param pos: A tuple representing The ship's head's (x, y) position
        :param length: Ship's length
        :param direction: Initial direction in which the ship is sailing
        :param board_size: Board size in which the ship is sailing
        """
        self.__pos = pos
        self.__length = length
        self.__direction = direction
        self.__board_size = board_size
        self.__damage_cells = []
        self.__damage_ship_cells = []
        self.__temp_direction = direction
        self.__coordinates = []

    def get_damage_ship_cells(self):
        return self.__damage_ship_cells

    def __repr__(self):
        """
        Return a string representation of the ship.
        :return: A tuple converted to string. The tuple's content should be (in
        the exact following order):
            1. A list of all the ship's coordinates.
            2. A list of all the ship's hit coordinates.
            3. Last sailing direction.
            4. The size of the board in which the ship is located.
        """
        coordinates = self.coordinates()
        ship_tuple = (coordinates, self.__damage_ship_cells,
                      ship_helper.direction_repr_str(Direction,
                                                     self.__temp_direction),
                      self.__board_size)
        return str(ship_tuple)

    def move(self):
        """
        Make the ship move one board unit.
        Movement is in the current sailing direction, unless such movement
        would take it outside of the board in which case the shp switches
        direction and sails one board unit in the new direction.
        the ship
        :return: A direction object representing the current movement
        direction.
        """
        if len(self.__damage_ship_cells) == 0:

            if self.__temp_direction == Direction.UP:
                if self.__pos[1] != 0:
                    new_pos_up = (self.__pos[0], self.__pos[1] - 1)
                    self.__pos = new_pos_up
                else:
                    self.__temp_direction = Direction.DOWN
                    new_pos_down = (self.__pos[0], self.__pos[1] + 1)
                    self.__pos = new_pos_down
                self.__coordinates = self.coordinates()
                return self.__temp_direction

            elif self .__temp_direction == Direction.DOWN:
                if self.__pos[1] + self.__length != self.__board_size:
                    new_pos_down = (self.__pos[0], self.__pos[1] + 1)
                    self.__pos = new_pos_down
                else:
                    self.__temp_direction = Direction.UP
                    new_pos_up = (self.__pos[0], self.__pos[1] - 1)
                    self.__pos = new_pos_up
                self.__coordinates = self.coordinates()
                return self.__temp_direction

            elif self .__temp_direction == Direction.LEFT:
                if self.__pos[0] != 0:
                    new_pos_left = (self.__pos[0] - 1, self.__pos[1])
                    self.__pos = new_pos_left
                else:
                    self.__temp_direction = Direction.RIGHT
                    new_pos_right = (self.__pos[0] + 1, self.__pos[1])
                    self.__pos = new_pos_right
                self.__coordinates = self.coordinates()
                return self.__temp_direction

            elif self .__temp_direction == Direction.RIGHT:
                if self.__pos[0] + self.__length != self.__board_size:
                    new_pos_right = (self.__pos[0] + 1, self.__pos[1])
                    self.__pos = new_pos_right
                else:
                    self.__temp_direction = Direction.LEFT
                    new_pos_left = (self.__pos[0] - 1, self.__pos[1])
                    self.__pos = new_pos_left
                self.__coordinates = self.coordinates()
                return self.__temp_direction

        else:
            return self.__temp_direction

    def hit(self, pos):
        """
        Inform the ship that a bomb hit a specific coordinate. The ship updates
         its state accordingly.
        If one of the ship's body's coordinate is hit, the ship does not move
         in future turns. If all ship's body's coordinate are hit, the ship is
         terminated and removed from the board.
        :param pos: A tuple representing the (x, y) position of the hit.
        :return: True if the bomb generated a new hit in the ship, False
         otherwise.
        """
        # if pos not in self.__damage_cells:
        #     self.__damage_cells.append(pos)
        if self.__contains__(pos) and pos not in self.__damage_ship_cells:
            self.__damage_ship_cells.append(pos)
            self.__temp_direction = Direction.NOT_MOVING
            return True
        else:
            return False



    def terminated(self):
        """
        :return: True if all ship's coordinates were hit in previous turns,
        False otherwise.
        """
        if (len(self.__damage_ship_cells) == self.__length):
            return True
        else:
            return False

    def __contains__(self, pos):
        """
        Check whether the ship is found in a specific coordinate.
        :param pos: A tuple representing the coordinate for check.
        :return: True if one of the ship's coordinates is found in the given
        (x, y) coordinates, False otherwise.
        """
        if pos in self.__coordinates:
            return True
        else:
            return False

    def coordinates(self):
        """
        Return ship's current positions on board.
        :return: A list of (x, y) tuples representing the ship's current
        position.
        """
        pos_list = []
        if self.__temp_direction in Direction.VERTICAL:
            for i in range(self.__length):
                vertical_pos = (self.__pos[0], self.__pos[1] + i)
                pos_list.append(vertical_pos)

        elif self.__temp_direction in Direction.HORIZONTAL:
            for i in range(self.__length):
                horizontal_pos = (self.__pos[0] + i, self.__pos[1])
                pos_list.append(horizontal_pos)
        else:
            return self.__coordinates
        self.__coordinates = pos_list
        return pos_list

    def damaged_cells(self):
        """
        Return the ship's hit positions.
        :return: A list of tuples representing the (x, y) coordinates of the
         ship which were hit in past turns (If there are no hit coordinates,
         return an empty list). There is no importance to the order of the
         values in the returned list.
        """
        return copy.deepcopy(self.__damage_ship_cells)

    def direction(self):
        """
        Return the ship's current sailing direction.
        :return: One of the constants of Direction class :
         [UP, DOWN, LEFT, RIGHT] according to current
         sailing direction or NOT_MOVING if the ship is hit and not moving.
        """
        if len(self.__damage_ship_cells) == self.__length:
            return Direction.NOT_MOVING
        else:
            return self.__temp_direction

    def cell_status(self, pos):
        """
        Return the state of the given coordinate (hit\not hit)
        :param pos: A tuple representing the coordinate to query.
        :return:
            if the given coordinate is not hit : False
            if the given coordinate is hit : True
            if the coordinate is not part of the ship's body : None 
        """
        pos_list = self.coordinates()
        if pos in pos_list:
            if pos in self.__damage_ship_cells:
                return True
            else:
                return False
        else:
            return None

