#!/usr/bin/env python
from FocusGame import FocusGame
import os


def main():

    exit_script = False
    print("Welcome to the Domination Focus Game")

    # loop for new game
    while not exit_script:
        # initialize game
        player1 = input("Enter Player1's Name: ")
        player2 = input("Enter Player2's Name: ")
        game = FocusGame((player1, 'R'), (player2, 'G'))
        game_over = False
        print(player1, "is Red and", player2, "is Green.")
        player = player1

        # game instance
        while not game_over:
            game.printBoard()
            reset = False

            # player1 turn
            # take player input and make terminal prompt
            if game.show_turn() % 2 != 0:
                player = player1
            else:
                player = player2

            print("Enter: 1: Normal Move, 2: Reserve Move, 3: Display Capture/Reserves")
            user_input = input(player + "'s move: ").strip()

            # if 1 2 3
            if int(user_input) == 1:
                print("enter start coordinates, end coordinates and piece number: (0,1) (0,2) 1")
                user_input = input("")
                move = user_input.strip().split(' ')
                print(game.move_piece(player, eval(move[0]), eval(move[1]), int(move[2])))

            elif int(user_input) == 2:
                print("enter coordinates to place reserve: (0,1)")
                user_input = input("move: ")
                move = user_input.strip()
                print(game.reserved_move(player, eval(move)))
            elif int(user_input) == 3:
                print("Captured: ", game.show_captured(player), "Reserve: ", game.show_reserve(player))
            else:
                print("invalid user input")

            # instance exit condition
            if game.show_status():
                game_over = True

        # post game prompt for user input to start another game or quit
        user_input = input("Enter 1 for new game or 2 for exit game: ").strip()
        if int(user_input) == 2:
            exit_script = True


if __name__ == "__main__":
    main()
