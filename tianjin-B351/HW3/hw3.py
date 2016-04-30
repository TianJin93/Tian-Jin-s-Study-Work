from chompUtilities import *
from chomp import *

def finished(x,y,board):
    rest = makeMove(x,y,board)
    for col in xrange(width):
        for row in xrange(height):
            if rest[col][row] == " ":
                return False
    return True

def heuristic1(board):
    boardvalue = width*height - len(board)
    if finished(x,y,board):
        return -boardvalue
    else:
        return 0

def alphabeta(board, depth,alpha,beta,maximizingPlayer):
    best_move = 0
    if depth <=0:
        return (heuristic1(alpha, best_move,board),0)

    for (x,y) in getValidMoves(board):
        makeMove(x,y,board)
        (value, junk) = alphabeta(board,depth-1,(-beta),(-alpha))
        value = -value
        if value >= beta:
            return (value,best_move)
        if value > alpha:
            (alpha,best_move) = (value,best_move)
    return (alpha, best_move)



def myPlayer(board):
    validmoves = getValidMoves(board)
    if isValidMove(x,y,board):
        board[y][x] = " "
    else:
        print "The move is not valid"
    return (y,x)