from chompUtilities import getValidMoves
import random

def randomMove(board):
    # Selects a random move from the list of all valid moves
    return random.choice(getValidMoves(board))