#check current state of the game board 
def evaluate(board):
    if 'xxx' in board:
        return 'x'
    elif 'ooo' in board:
        return 'o'
    elif '-' not in board:
        return '!'
    else:
        return '-'


# make a move
def move(board, mark, position):
    if board[position] == '-':
        return board[:position] + mark + board[position+1:]
    return board


# Player's move
def player_move(board, mark):
    while True:
        try:
            position = int(input(f"Enter the position (0-19) for {mark}: "))
            if position < 0 or position > 19:
                print("Position must be between 0 and 19.")
            elif board[position] != '-':
                print("Position already occupied.")
            else:
                return move(board, mark, position)
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 19.")


# Computer's move
import random

def pc_move(board, mark):
    while True:
        position = random.randint(0, 19)
        if board[position] == '-':
            return move(board, mark, position)


# main function
def tictactoe_1d():
    board = '-' * 20
    current_mark = 'x'
    
    while True:
        print(f"Current board: {board}")
        if current_mark == 'x':
            board = player_move(board, current_mark)
        else:
            board = pc_move(board, current_mark)
        
        game_state = evaluate(board)
        if game_state == 'x':
            print(f"Current board: {board}")
            print("Player X wins!")
            break
        elif game_state == 'o':
            print(f"Current board: {board}")
            print("Player O wins!")
            break
        elif game_state == '!':
            print(f"Current board: {board}")
            print("It's a draw!")
            break
        
        current_mark = 'o' if current_mark == 'x' else 'x'


# Run the game
tictactoe_1d()



