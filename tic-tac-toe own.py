# -*- coding: utf-8 -*-
"""

@author: afaan

PROGRAM:- TIC TAC TOE
"""


maxPlayer, minPlayer = 'x', 'o'

def evaluate(board):
    if all([board[i][j] == ' ' for i in range(3) for j in range(3)]):
        # if all the places 
        return 0

    if ['x']*3 in board:
        return 10

    if ['o']*3 in board:
        return -10
    
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[1][col] != ' ':
            return 10 if board[1][col] == 'x' else -10
    
    if len(set([board[i][i] for i in range(3)])) == 1 and board[1][1] != ' ':
        return 10 if board[1][1] == 'x' else -10
    
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[1][1] != ' ':
        return 10 if board[1][1] == 'x' else -10
    
    return 0


def game_over(board):
    if(evaluate(board) == 10 or evaluate(board)  == -10):
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False

    return True


def minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    
    if game_over(board):
        return 0
    
    if isMax:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = maxPlayer
                    best_score = max(best_score, minimax(board, depth+1, not isMax))
                    board[i][j] = ' '
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = minPlayer
                    best_score = min(best_score, minimax(board, depth+1, not isMax))
                    board[i][j] = ' '
        return best_score


def findBestMove(board, isMax):
    bestVal = -1000 if isMax else 1000
    # bestVal = -1000, if X's turn (max player) else it is Y's turn
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                board[i][j] = maxPlayer if isMax else minPlayer

                moveVal = minimax(board, 0, not isMax)

                board[i][j] = ' '

                if (isMax and moveVal > bestVal) or (not isMax and moveVal < bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    
    return bestMove


def printBoard(board):
    print()
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(f" {board[i][j]} ")
            else:
                print(f" {board[i][j]} ", end='|')
        if i != 2:
            print("---+---+---")
    print()


if __name__ == "__main__":
    board = [
        [ ' ', ' ', ' ' ],
        [ ' ', ' ', ' ' ],
        [ ' ', ' ', ' ' ]
    ]
    printBoard(board)
    print("Hello User! Welcome")

    choice = -1
    while choice not in ['x', 'o']:
        print("Play as [x/o]: ", end='')
        choice = input().strip()
    if choice == 'x':
        user, pc = 'x', 'o'
        isMax = False
    else:
        user, pc = 'o', 'x'
        isMax = True

    
    choice = -1
    while choice not in ['y', 'n']:
        print("Do you want to make first move? [y/n]: ", end='')
        choice = input().strip()

    turn = "user"
    if choice == 'n':
        board[0][0] = pc
        printBoard(board)
        turn = "user"
    

    while not game_over(board):
        if turn == "user":
            while True:
                print("Enter position to place", user)
                position_x, position_y = map(int, input().strip().split(" "))
                if (position_x, position_y) != (-1, -1) and board[position_x][position_y] == ' ':
                    break
                print("The position is already occupied")
            board[position_x][position_y] = user
        else:
            bestMove = findBestMove(board, isMax)
            board[bestMove[0]][bestMove[1]] = pc
        
        turn = "user" if turn == "pc" else "pc"
        printBoard(board)
    
    if(evaluate(board) == 10 or evaluate(board)  == -10):
        print("x won" if evaluate(board) == 10 else "y won")
    else:
        print("Game drawn!")
