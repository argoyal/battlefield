"""
battleship game
"""


class Ship(object):
    """
    ship class creates ship objects
    with their name and positions
    """

    SHIP_NAME_SIZE_COUNT = {
        "Destroyer": 2,
        "Submarine": 3,
        "Battleship": 4,
        "Aircraft Carrier": 5,
    }

    def __init__(self):
        print "\n the ships which are available are: \n"
        for ship_name, ship_size in self.SHIP_NAME_SIZE_COUNT.iteritems():
            print "{0:30} {1}".format(ship_name, ship_size)

        self.ship_name = raw_input("\nwhich ship do you want to place? \n")
        self.ship_location = raw_input(
            "enter ship location: rowxcolumn| for vertical, rowxcolumn-" +
            " for horizontal: \n"
        )

    def get_ship_coordinates(self):
        ship_coordinates = []
        ship_size = self.SHIP_NAME_SIZE_COUNT[self.ship_name]

        if self.ship_location[-1] == "|":
            coordinates = self.ship_location.split("|")[0]
            row = int(coordinates.split("x")[0]) - 1
            column = int(coordinates.split("x")[1]) - 1

            for i in range(ship_size):
                ship_coordinates.append((row+i, column))

        if self.ship_location[-1] == "-":
            coordinates = self.ship_location.split("-")[0]
            row = int(coordinates.split("x")[0]) - 1
            column = int(coordinates.split("x")[1]) - 1

            for i in range(ship_size):
                ship_coordinates.append((row, column+i))

        return ship_coordinates


class Board(object):
    """
    board class which holds properties
    of player's board
    """

    BOARD_SIZE = 0

    def __init__(self):
        self.board_size = self.BOARD_SIZE
        self.board_status = self.create_new_board()

    def create_new_board(self):
        new_board = []

        for i in range(self.board_size):
            new_board.append(['.']*9)

        return new_board

    def print_board_status(self):
        print "\n ===> current board status for player {}".format(
            self.__class__.__name__.replace("Board", ""))

        for row in self.board_status:
            print " ".join(row)

        print "\n"

    def place_ship(self, ship):
        coordinates = ship.get_ship_coordinates()

        for coordinate in coordinates:
            row = coordinate[0]
            column = coordinate[1]

            current_status = self.board_status[row][column]

            """
            currently updating as is in the loop shouldn't be that way
            if even one of the coordinates overlap should place the
            entire ship object
            """

            if current_status == ".":
                self.board_status[row][column] = "0"
            else:
                print "a ship is already placed here... handle error"
                continue

        self.print_board_status()

    def update_positions_by_gameplay(self):
        """
        update the position when the user plays the game
        the entire game should be played using the game
        object

        should be implemented here.
        """

        pass


class Game(object):
    """
    the gameplay class which navigates the entire
    game play
    """

    def __init__(self):
        self.size = int(raw_input("enter the battleship board size: "))
        self.no_users = int(raw_input(
            "enter the number of players playing the game: "))

        self.boards = {}

        for i in range(self.no_users):
            player_name = raw_input("enter player name: ")
            board = self.setup_board(player_name)()

            self.boards.update({
                player_name: board
            })

            board.print_board_status()

        for player_name, player_board in self.boards.iteritems():
            print "place ships on board for {}\n".format(player_name)
            continuation = True

            while continuation:
                ship = Ship()
                player_board.place_ship(ship)

                user_input = raw_input("do you want to place more ships (Y/N)")
                if user_input == "Y":
                    continue
                else:
                    continuation = False

    def setup_board(self, player_name):
        print "setting up board for {}\n".format(player_name)

        board = type("{}Board".format(player_name), (Board,),
                     {"BOARD_SIZE": self.size})

        return board

    def die_throw(self):
        """
        deciding which player goes first
        """
        pass

    def play(self, player_name, coordinates):
        """
        takes in the coordinates and decide what
        action be taken on the board object
        """
        pass


if __name__ == "__main__":
    game = Game()

    """
    the entire game logic remains
    should be implemented to complete the game
    """
