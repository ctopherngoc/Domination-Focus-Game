This Domination Focus Game Project is a game that allows two players to emulate the Domination Focus board game.

This implementation of the game with a 6x6 board. The traditional game has 16 extra board space (four on each board side.)

Prerequisites
Before you begin, ensure you have met the following requirements:

You have installed the latest version of Python and/or Python IDE such as Pycharm or Atom.
You have a Windows or Mac machine (have not tried with Linux).
You have read documentation for this project.
You have read rule-set/how to play the Domination Focus Game (stated below).
Installing Domination Focus Game
To install Domination Focus Game, follow these steps:

macOS:
1. Locate the Terminal app within the LaunchPad or use IDE terminal.
2. Go to specific folder where you want the repository to be saved.
3. Clone Repository by running following in Terminal: git clone git@github.com:ctopherngoc/Domination-Focus-Game.git
4. Locate and change directories to the directory containing the cloned repository.
5. Run the following line in the Terminal: python3 runGame.py

Windows:
1. Click on the searchbar on the bottom left and search and open the Command Prompt.
2. Go to specific folder where you want the repository to be saved.
3. Clone Repository by running following in Terminal: git clone https://github.com/ctopherngoc/Domination-Focus-Game.git
4. Locate and change directories to the directory containing the cloned repository.
5. Run the following line in the Terminal: python3 runGame.py

Rules: How to Play
When runGame.py starts, you will be greeted with a welcome message and be prompted to enter player1 and player 2 names.
At the start of each turn, the current board status and the current player's turn and captured/reserves will be displayed.
The player will be prompted to enter 1. Normal Move or 2. Reserve Move. The rules for the following moves:

Normal Move:
1. Players may only move from board spaces where their piece is on top of a stack of pieces.
   (Player1 = "R", Player2 = "G")
2. Players are allowed to move Up, Down, Left, Right directions (no diagonal)
3. If board location has a stack (two or more pieces), you are allowed to move up to that many pieces in one move.
4. In addition, the prior, you are allowed to move up to the amount of spaces based on the amount of peaces being moved.
   Example: A stack of 4 pieces can move between 1-4 pieces. Of a stack of 5 pieces, 4 can be moved 1-4 spaces.

Reserve Move:
1. Player must have at least one piece in reserve for successful move.
2. Reserve moves allow a reserved piece to be play on top of any board space.
3. This takes up a turn.

Upon entering the move you want to perform, the player will be prompted to input information on the move based on
what was chosen. The board location is based on (X,Y) coordinates between 0 and 5. Most top-right space is (0,0)
and most bottom-right space is (5,5). The following format for each move is:

Normal Move:
(Starting Location) (Ending Location) # of pieces
EX: (0,5) (5,5) 5 </br>
    (0,0) (0,1) 1 </br>
    (3,2) (1,2) 4

Reserve Move:
(Board Location)
EX: (5,5) </br>
    (4,3) </br>
    (0,0)

Unsuccessful moves will be displayed and current player will be prompted to re-enter move. Players will take turn making
moves until one captures at least six enemy pieces. Once a player wins, the players will be prompted to play another 
game or close the program.


Contact
If you want to contact me you can reach me at ctopherngoc@gmail.com.
