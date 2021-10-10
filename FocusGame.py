# The program simulates the focus game as a 6x6 board.
class FocusGame:
    def __init__(self, player1, player2):
        """
        Initialize the board for the focus game.
        """

        self._player1 = player1
        self._player2 = player2
        self._turncounter = 1  # player1 moves on odds, player2 moves on evens

        self._dict = {
            self._player1[0]: {"user": self._player1[0], "piece": self._player1[1], "captured": 0, "reserved": 0},
            self._player2[0]: {"user": self._player2[0], "piece": self._player2[1], "captured": 0, "reserved": 0}}
        counter = 0

        # boolean win condition
        self._win = 0

        # creates 8x8 board
        self._main_board = [[] for x in range(6)]
        while counter <= 5:
            for row in self._main_board:
                self._main_board[counter] = [[""] for y in range(6)]
                counter += 1
        self.fillBoard()

    def fillBoard(self):
        """
        Fills the board with player pieces.
        """
        # set initial conditions for while loop
        row = 0
        column = 0
        red_counter = 0
        green_counter = 0

        # populates board with green and red markers
        while row < 6:
            while column < 6:
                if red_counter < 2:
                    self._main_board[row][column][0] = "R"
                    red_counter += 1
                    column += 1

                elif green_counter < 2:
                    self._main_board[row][column][0] = "G"
                    green_counter += 1
                    column += 1
                else:
                    red_counter = 0
                    green_counter = 0
            row += 1
            column = 0

    def printBoard(self):
        """
        prints board by rows.
        """
        for row in self._main_board:
            print(row)

    def show_reserve(self, player):
        """
        returns the player's reserved pieces
        """
        return self._dict[player]["reserved"]

    def show_captured(self, player):
        """
        returns the player's captured pieces
        """
        return self._dict[player]["captured"]

    def show_pieces(self, position):
        """
        returns the list representing the coordinates on the board containing the stack pieces
        """
        return self._main_board[position[0]][position[1]]

    def post_move(self, player, end):
        """
            Method for scripts post move. Moves pieces into reserve and captured. Verifies if win conditions are met.
            """

        end_point = self._main_board[end[0]][end[1]]
        while len(end_point) > 5:
            if end_point[0] == self._dict[player]["piece"]:
                self._dict[player]["reserved"] += 1
                end_point[:] = end_point[1:]
            else:
                self._dict[player]["captured"] += 1
                end_point[:] = end_point[1:]

    def move_piece(self, player, start, end, piece):
        """
        Method  for single and multiple moves.Containing series of conditionals to determine if move is appropriate.
        Returns statements if conditionals are not met. If conditionals are met, moves pieces from start to end
        position then calls post_move method.
        """
        # create variables containing long repetitive references to the board
        start_point = self._main_board[start[0]][start[1]]
        end_point = self._main_board[end[0]][end[1]]

        # win condition check
        if self._win != 1:

            # check if correct player's turn player1 = odd, player2 = even
            if (player == self._player1[0] and self._turncounter % 2 != 0) or (
                    player == self._player2[0] and self._turncounter % 2 == 0):

                # check if amount of piece is <= to pieces at start location and distance move = pieces moved
                if piece <= len(start_point) and (abs(end[0] - start[0]) == piece or abs(end[1] - start[1]) == piece):

                    # check if move is valid
                    if start != end:

                        # if player's piece is on top of start stack
                        if start_point[-1] == self._dict[player]["piece"]:

                            # temp list hold pieces to move
                            temp_list = self._main_board[start[0]][start[1]][-piece:]

                            # remove pieces from start
                            self._main_board[start[0]][start[1]] = start_point[:len(start_point) - piece]

                            # extend end point with pieces
                            end_point.extend(temp_list)

                            # increment turn counter
                            self._turncounter += 1

                            # if stack is > 5, calculate reserve and capture checks win condition
                            if len(end_point) > 5:
                                self.post_move(player, end)
                                if self._dict[player]["captured"] >= 6:
                                    self._win = 1
                                    return player + " Wins"

                            return "successfully moved"

                        else:
                            return "invalid piece"
                    else:
                        return "invalid location"
                else:
                    return "invalid number of pieces"
            else:
                return "not your turn"
        else:
            return False

    def reserved_move(self, player, location):
        """
        Method for using pieces in reserve bank to place on board. After conditionals are met and move occurred.
        Increments turncounter and calls post_move method for victory validation if the.
        """
        end_point = self._main_board[location[0]][location[1]]

        if self._win != 1:

            # checks if player reserved list != 0
            if self._dict[player]["reserved"] >= 1:

                # decrement player reserve and extends location
                self._dict[player]["reserved"] -= 1
                end_point.extend(self._dict[player]["piece"])
                self.post_move(player, location)

                self._turncounter += 1

                # calls post_move method if pieces > 5 and checks win condition
                if len(end_point) > 5:
                    while len(end_point) > 5:
                        self.post_move(player, location)
                        if self._dict[player]["captured"] >= 6:
                            self._win = 1
                            return player + " Wins"
                return "successfully moved"
            else:
                return "no pieces in reserved"
        else:
            return False
