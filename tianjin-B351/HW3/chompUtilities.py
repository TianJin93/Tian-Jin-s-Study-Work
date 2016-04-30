
def printBoard(board):
    # Prints out the given game board
    for rowNum,row in enumerate(board):
            printerRow = [elem for elem in row]
            printerRow.append(rowNum)
            print printerRow
    print([str(i) for i in range(len(board[0]))])

def getValidMoves(board):
    # Enumerates a list of all valid moves on the board, as tuples of the form (x,y) 
    validMoves = [(x,y) for y,row in enumerate(board) for x,elem in enumerate(row) if elem != " "]
    if validMoves != [(0,0)]: validMoves.remove((0,0))
    return validMoves

def makeMove(x,y,board):
    # Checks if a move is valid, then returns the state of the board after the move has been made
    # If the move is invalid, the (0,0) position will be set to " "
    # NOTE: This fuction returns a board - it does not modify the given board
    if isValidMove(x,y,board):
            return [[" " if elemNum >= x and rowNum >=y else elem for elemNum,elem in enumerate(row)] for rowNum,row in enumerate(board)]
    else:
            print("invalid move (%d,%d)" % (x,y))
            # force defeat for the player that made the invalid move
            board[0][0] = " "
            return board

def isValidMove(x,y,board):
    # Checks if a given position is valid
    # Returns boolean True if the position is valid, and boolean False if the move is not valid
    if board[y][x] == " ":
            print "position already played"
            return False
    if x > len(board[0]) or y > len(board):
            print "position outside of board"
            return False
    return True