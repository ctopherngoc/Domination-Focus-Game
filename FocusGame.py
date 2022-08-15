# The program simulates the domination focus game as a 6x6 board.
class FocusGame:
    def __init__(self, player1, player2):
        """
        Initialize the board for the focus game.
        """

        self._player1 = player1
        self._player2 = player2
        self._win = 0
        self._turncounter = 1  # player1 moves on odds, player2 moves on evens

        self._dict = {
            self._player1[0]: {"user": self._player1[0], "piece": self._player1[1], "captured": 0, "reserved": 0},
            self._player2[0]: {"user": self._player2[0], "piece": self._player2[1], "captured": 0, "reserved": 0}}

        self._main_board = [[] for x in range(6)]

        for y in range(6):
            if y % 2 == 0:
                self._main_board[y] = [['G'], ['G'], ['R'], ['R'], ['G'], ['G']]
            else:
                self._main_board[y] = [['R'], ['R'], ['G'], ['G'], ['R'], ['R']]

    def printBoard(self):
        """
        helper function: prints board by rows.
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
            Method for scripts post move. Move pieces into reserve and captured. Verifies if win conditions are met.
            """

        end_point = self._main_board[end[0]][end[1]]
        while len(end_point) > 5:
            if end_point[0] == self._dict[player]["piece"]:
                self._dict[player]["reserved"] += 1
                end_point[:] = end_point[1:]
            else:
                self._dict[player]["captured"] += 1
                end_point[:] = end_point[1:]

    def valid_move_check(self, player, start, end, piece):
        """
        Helper function: checks valid movement then if player's piece is on top of stack.
        """
        start_point = self._main_board[start[0]][start[1]]
        end_point = self._main_board[end[0]][end[1]]

        if start == end:
            return False

        # x axis movement
        if abs(end[0] - start_point[0]) == piece and end_point[1] == start_point[1]:
            if start_point[-1] == self._dict[player]["piece"]:
                return True

        # y axis movement
        elif abs(end[1] - start_point[1]) == piece and end_point[0] == start_point[0]:
            if start_point[-1] == self._dict[player]["piece"]:
                return True

        return False

    def player_turn_check(self, player):
        if (player == self._player1[0] and self._turncounter % 2 != 0) or (
                player == self._player2[0] and self._turncounter % 2 == 0):
            return True
        else:
            return False

    def stack_check(self, start, piece):
        if piece <= len(self._main_board[start[0]][start[1]]):
            return True
        else:
            return False

    def coord_check(self, start, end):
        """
        Helper Function: checks coordinates are valid on board.
        """
        if start[0] < 0 or start[0] > 5:
            return False
        elif start[1] < 0 or start[1] > 5:
            return False
        elif end[0] < 0 or end[0] > 5:
            return False
        elif end[1] < 0 or end[1] > 5:
            return False
        else:
            return True

    def move_piece(self, player, start, end, piece):
        """
        Method for single and multiple moves. If conditionals are met, moves piece(s).
        """

        # win condition check
        if self._win == 1:
            return "Game finished"

        if not self.coord_check(start, end):
            return "invalid coordinates"

        # create variables containing long repetitive references to the board
        start_point = self._main_board[start[0]][start[1]]
        end_point = self._main_board[end[0]][end[1]]

        if not self.player_turn_check(player):
            return "not your turn"

        if not self.stack_check(start, piece):
            return "invalid number of pieces"

        if not self.valid_move_check(player, start, end, piece):
            return "invalid move"

        # temp list hold pieces to move. reverse slice list
        temp_list = start_point[-piece:]

        # remove pieces from start
        self._main_board[start[0]][start[1]] = start_point[:len(start_point) - piece]

        # extend end point with pieces
        end_point.extend(temp_list)

        # increment turn counter
        self._turncounter += 1

        if len(end_point) > 5:
            self.post_move(player, end)
            if self._dict[player]["captured"] >= 6:
                self._win = 1
                return player + " Wins"

    def reserved_move(self, player, location):
        """
        Method for using pieces in reserve bank to place on board. After conditionals are met and move occurred.
        Increments turn counter and calls post_move method for victory validation if the.
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
