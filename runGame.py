#!/usr/bin/env python
from FocusGame import FocusGame


def move_input_check(input_list):
    numbers = "01234567890(),"

    # correct length 3
    if len(input_list) != 3:
        return False

    # character check
    for index in input_list:
        for char in index:
            if char not in numbers:
                return False

    # create tuple, convert to ints
    start = eval(input_list[0])

    # value check
    for x in start:
        if type(x) is int:
            if 0 > x > 5:
                return False
        else:
            return False

    end = eval(input_list[1])
    for x in end:
        if type(x) is int:
            if 0 > x > 5:
                return False
        else:
            return False

    # still string
    if input_list[2] not in numbers:
        return False

    # create int
    number = int(input_list[2])
    if 0 < number > 5:
        return False

    # pass input check
    return True


def reserve_move_check(input_list):
    numbers = "0123456789(),"
    if len(input_list) != 1:
        print(len(input_list))
        print("length issue")
        return False

    for x in input_list[0]:
        if x not in numbers:
            return False

    start = eval(input_list[0])
    for x in start:
        if type(x) is int:
            if 0 > x > 5:
                print("int not 0-5")
                return False
        else:
            print("not int")
            return False

    return True


def player_turn(game, player):
    user_input = input(player + ": 1.Normal Move 2.Reserve Move ")

    if user_input not in ['1', '2']:
        print("Invalid choice. Try again.")
        return False

    elif int(user_input) == 1:
        user_input = input("Enter start, end, and quantity: (0,1) (0,2) 1: ")
        move = user_input.strip().split(' ')
        if not move_input_check(move):
            print("Invalid user input. Try again.")
            return False

        else:
            if game.move_piece(player, eval(move[0]), eval(move[1]), int(move[2])):
                print("Successful move")
                return True
            else:
                print("Unsuccessful move")
                return False

    elif int(user_input) == 2:
        print("Enter location for reserved move: (0,1)")
        user_input = input("move: ")
        move = user_input.strip().split(' ')

        if not reserve_move_check(move):
            print("Invalid user input. Try again.")
            return False

        else:
            if game.reserved_move(player, eval(move[0])):
                print("Successful move")
                return True
            else:
                print("Unsuccessful move")
                return False
    else:
        print("Invalid input. Try again.")
        return False


def new_game():
    player1 = input("Enter Player1's Name: ").strip()
    player2 = input("Enter Player2's Name: ").strip()
    game = FocusGame((player1, 'R'), (player2, 'G'))
    print(player1, "is Red and", player2, "is Green.")
    return game, player1, player2


def pre_move(game, player1, player2):
    if game.show_turn() % 2 != 0:
        player = player1
    else:
        player = player2

    game.printBoard()
    print(player, "turn: Captured: ", game.show_captured(player), "Reserve: ", game.show_reserve(player))
    return player, False


def main():
    exit_script = False
    print("Welcome to the Domination Focus Game")

    # loop for new game
    while not exit_script:
        # initialize game
        game, player1, player2 = new_game()
        game_over = False

        # game instance
        while not game_over:
            player, turn_over = pre_move(game, player1, player2)

            # turn instance
            while not turn_over:
                if player_turn(game, player):
                    turn_over = True

            # instance exit condition
            if game.show_status():
                game_over = True

        # post game prompt for user input to start another game or quit
        print(player, "Wins!")
        user_input = input("Enter 1 for new game or 2 for exit game: ").strip()
        if int(user_input) == 2:
            exit_script = True


if __name__ == "__main__":
    main()
