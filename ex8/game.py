############################################################
# Imports
############################################################
import game_helper as gh
############################################################
# Class definition
############################################################


class Game:
    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """

    def __init__(self, board_size, ships):
        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board
        :param ships: A list of ships that participate in the game.
        :return: A new Game object.
        """
        self.__board_size = board_size
        self.__ships = ships
        self.__damaged_ships = []
        self.__terminated_ships = []
        self.__bomb_on_board = {}
        self.__healthy_ships = []
        self.__hit_ship_cells = []

    def __play_one_round(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        Te function runs one round of the game :
            1. Get user coordinate choice for bombing.
            2. Move all game's ships.
            3. Update all ships and bombs.
            4. Report to the user the result of current round (number of hits and
             terminated ships)
        :return:
            (some constant you may want implement which represents) Game status :
            GAME_STATUS_ONGOING if there are still ships on the board or
            GAME_STATUS_ENDED otherwise.
        """
        new_bomb = gh.get_target(self.__board_si



        ze)
        self.__bomb_on_board[new_bomb] = 4
        self.ship_mover()
        self.damaged_ships()
        self.bombs_life_time()
        hits = self.last_hit()
        self.remove_items(hits[0])
        self.not_damaged_pos()
        self.damaged_pos()
        terminations = self.terminated_ships()
        gh.report(gh.board_to_string(self.__board_size, hits[0],
                                     self.__bomb_on_board,
                                     self.__hit_ship_cells,
                                     self.__healthy_ships))
        gh.report_turn(hits[1], terminations)

    def __repr__(self):
        """
        Return a string representation of the board's game
        :return: A tuple converted to string. The tuple should contain (maintain
        the following order):
            1. Board's size.
            2. A dictionary of the bombs found on the board
                 {(pos_x, pos_y) : remaining turns}
                For example :
                 {(0, 1) : 2, (3, 2) : 1}
            3. A list of the ships found on the board (each ship should be
                represented by its __repr__ string).
        """
        game_tuple = (self.__board_size, self.__bomb_on_board, self.__ships)
        return str(game_tuple)

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        completion.
        :return: None
        """
        gh.report_legend()
        all_ships_coordinates = []
        for ship in self.__ships:
            all_ships_coordinates += ship.coordinates()
        print(gh.board_to_string(self.__board_size, [], self.__bomb_on_board,
                                 [], all_ships_coordinates))
        while len(self.__ships) != 0:
            self.__play_one_round()
        gh.report_gameover()

    def ship_mover(self):
        """
        move the ships using move() in class ship
        """
        for ship in self.__ships:
            ship.move()

    def damaged_ships(self):
        for ship in self.__ships:
            if len(ship.damaged_cells()) != 0:
                self.__damaged_ships.append(ship)

    def terminated_ships(self):
        """
        remove ships that were hit in all of their cells
        :return: terminated_counter - num of terminated ships
        """
        terminated_counter = 0
        for ship in self.__ships:
            if ship.terminated():
                terminated_counter += 1
                self.__terminated_ships.append(ship)
                self.__ships.remove(ship)
        return terminated_counter

    def bombs_life_time(self):
        """
        count down three turns for a single bomb and update
        self.__bomb_on_board
        """
        temp_bombs = {}
        for bomb in self.__bomb_on_board:
            if self.__bomb_on_board[bomb] != 1:
                self.__bomb_on_board[bomb] -= 1
                temp_bombs[bomb] = self.__bomb_on_board[bomb]
        self.__bomb_on_board = temp_bombs

    def damaged_pos(self):
        """
        append damaged positions of ships on the board
        """
        self.__hit_ship_cells = []
        for ship in self.__ships:
            for pos in ship.coordinates():
                if pos in ship.damaged_cells():
                    self.__hit_ship_cells.append(pos)

    def not_damaged_pos(self):
        """
        append non-damaged positions of ships on the board
        """
        self.__healthy_ships = []
        for ship in self.__ships:
            for pos in ship.coordinates():
                if pos not in ship.damaged_cells():
                    self.__healthy_ships.append(pos)

    def last_hit(self):
        """
        count the number of hits and returns a list of hits positions and
        the number of hits
        :return: a list of hits positions and the number of hits
        """
        hits = []
        hits_counter = 0
        for pos in self.__bomb_on_board:
            for ship in self.__ships:
                if ship.hit(pos):
                    hits.append(pos)
                    hits_counter += 1
        hits_count = [hits, hits_counter]
        return hits_count

    def remove_items(self, list_of_coordinates):
        """
        remove items from a given dictionary that appear in a given list
        :param list_of_coordinates: a list
        """
        for key in list_of_coordinates:
            if key in self.__bomb_on_board:
                del self.__bomb_on_board[key]

############################################################
# An example usage of the game
############################################################
if __name__=="__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()
