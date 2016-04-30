
from chompUtilities import printBoard,isValidMove,makeMove
from randomMove import randomMove as player1
from hw3 import myPlayer as player2

width = 5
height = 5
number_of_games = 100 # used for simulateGames

def playGame(quiet):
    # Creates a board, and plays a single game of Chomp, and returns the player number of the victor
    # Setting the quiet argument to True greatly speeds up execution at the expense of verbosity
    board = [["X" for _ in range(width)] for _ in range(height)]
    playerNum = 1
    while(board[0][0] != " "):
            if not quiet:
                printBoard(board)
                print("player " + str(playerNum) + "'s turn")
            nextMove = getNextMove(board,playerNum)
            if not quiet:
                print("player " + str(playerNum) + "'s move is: " + str(nextMove))
            board = makeMove(nextMove[0],nextMove[1],board)
            # get the next player num
            playerNum = 1 if playerNum == 2 else 2
    if not quiet:
        print("player " + str(playerNum) + " wins!")
    return playerNum

def getNextMove(board,playerNum):
    # Calls the requested player function between of two players
    # Player functions must return a tuple of the form (x,y)
    if playerNum == 1: return player1(board)
    if playerNum == 2: return player2(board)

def simulateGames(numOfGames):
    # Plays a given number of games, and outputs the final number of wins for player one
    results = [playGame(True) for _ in range(numOfGames)]
    print("Player one won " + str(results.count(1)) + " out of " + str(numOfGames) + " games.")

if __name__ == "__main__":
    simulateGames(number_of_games)