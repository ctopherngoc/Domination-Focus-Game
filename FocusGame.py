# The program simulates the domination focus game on a 6x6 board.
class FocusGame:
    def __init__(self, player1, player2):
        """
        Initialize the board 6x6 for the domination focus game.
        """
        self._player1 = player1
        self._player2 = player2
        self._win = False
        self._turncounter = 1

        self._dict = {
            self._player1[0]: {"user": self._player1[0], "piece": self._player1[1], "captured": 0, "reserved": 0},
            self._player2[0]: {"user": self._player2[0], "piece": self._player2[1], "captured": 0, "reserved": 0}}

        self._main_board = [[] for x in range(6)]

        for row in range(6):
            if row % 2 == 0:
                self._main_board[row] = [['R'], ['R'], ['G'], ['G'], ['R'], ['R']]
            else:
                self._main_board[row] = [['G'], ['G'], ['R'], ['R'], ['G'], ['G']]

    def printBoard(self):
        """
        Displays current board state.
        """
        for row in self._main_board:
            print(row)

    def show_reserve(self, player):
        """
        returns the player's reserved count.
        """
        return self._dict[player]["reserved"]

    def show_captured(self, player):
        """
        returns the player's captured count.
        """
        return self._dict[player]["captured"]

    def show_pieces(self, position):
        """
        Returns the list for the position on the board. Pieces are ordered from lowest to the highest in the stack.
        """
        return self._main_board[position[0]][position[1]]

    def post_move(self, player, end):
        """
            Helper Function: loops through destination stack post-move until pieces == 5.
            Remove pieces from the bottom of stack and increments captured/reserved count.
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
        Helper function: checks for valid movement and if player's piece is on top of stack.
        """
        start_point = self._main_board[start[0]][start[1]]

        if start == end:
            return False

        # x axis movement
        if abs(end[0] - start[0]) <= piece and end[1] == start[1]:
            if start_point[-1] == self._dict[player]["piece"]:
                return True

        # y axis movement
        elif abs(end[1] - start[1]) <= piece and end[0] == start[0]:
            if start_point[-1] == self._dict[player]["piece"]:
                return True

        return False

    def player_turn_check(self, player):
        """
        Helper Function: Checks correct player turn by comparing player input and turncounter.
        Player 1 = Odd, Player 2 = Even.
        """
        if (player == self._player1[0] and self._turncounter % 2 != 0) or (
                player == self._player2[0] and self._turncounter % 2 == 0):
            return True
        else:
            return False

    def stack_check(self, start, piece):
        """
        Helper Function: checks pieces to move is valid relative to stack of start location.
        """
        if piece <= len(self._main_board[start[0]][start[1]]):
            return True
        else:
            return False

    def coord_check(self, coord):
        """
        Helper Function: checks coordinates are valid on board.
        """
        if coord[0] < 0 or coord[0] > 5:
            return False
        elif coord[1] < 0 or coord[1] > 5:
            return False
        else:
            return True

    def move_piece(self, player, start, end, piece):
        """
        Method for single and multiple moves. If conditionals are met, moves piece(s).
        """

        if self._win:
            return "Game already over!"

        if not self.coord_check(start) or not self.coord_check(end):
            return "invalid start-end coordinates"

        # variables references
        start_point = self._main_board[start[0]][start[1]]
        end_point = self._main_board[end[0]][end[1]]

        if not self.player_turn_check(player):
            return "not your turn"

        if not self.stack_check(start, piece):
            return "invalid quantity of pieces entered"

        if not self.valid_move_check(player, start, end, piece):
            return "invalid move"

        # temp list hold pieces to move. reverse slice list
        temp_list = start_point[-piece:]

        # remove pieces from start
        self._main_board[start[0]][start[1]] = start_point[:len(start_point) - piece]

        # extend end point with pieces
        end_point.extend(temp_list)
        self._turncounter += 1

        # reserves/capture and win check
        if len(end_point) > 5:
            self.post_move(player, end)
            if self._dict[player]["captured"] >= 6:
                self._win = True
                return player + " Wins"

        return "Successful move"

    def reserved_move(self, player, location):
        """
        Place pieces from reserves on board.
        """

        if self._win:
            return "Game already over!"

        if not self.coord_check(location):
            return False

        if self._dict[player]["reserved"] == 0:
            return "no pieces in reserved"

        end_point = self._main_board[location[0]][location[1]]

        # decrement player reserve and extends location
        self._dict[player]["reserved"] -= 1
        end_point.extend(self._dict[player]["piece"])
        self.post_move(player, location)
        self._turncounter += 1

        # reserve_move places 1 piece on stack: max = 6
        if len(end_point) > 5:
            self.post_move(player, location)
            if self._dict[player]["captured"] >= 6:
                self._win = 1
                return player + " Wins"
        return "Successful reserved move"
