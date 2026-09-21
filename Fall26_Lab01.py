# 1. Name:
#      Alayna Earl
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      For me, the hardest part is when I had to do anything with the
#      JSON data. That part still doesn't automatically come to me. I
#      looked at old notes and past assignments. I'd work on it for a
#      bit and then I'd get help from ChatGPT. The desired structure
#      for the JSON data was particularly difficult. I don't have that
#      memorized. So both the reading and writing the file was
#      difficult for me, as well as working with the data in the
#      necessary structure.
# 5. How long did it take for you to complete the assignment?
#      4 hours 15 minutes

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def main():
    '''The main function serves to populate the necessary data to start
    the game and print the inital information to the user.'''
    # Get the data for the board from the JSON file.
    board_data_dict = read_board('Fall26_Lab01.json')

    if type(board_data_dict) != dict:
        save_board('Fall26_Lab01.json', blank_board)
        board_data_dict = read_board('Fall26_Lab01.json')

    # Take the data from being in a dictionary to being in a list
    # for ease of use.
    board_data = board_data_dict["board"]

    # These user-instructions are provided and do not need to be changed.
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")

    # Print an empty grid for a new game or load a previous saved game.
    display_board(board_data)
    play_game(board_data)


def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Read the board data from the JSON file.
    try:
        with open(filename, 'r') as file_data:
            board_data = json.load(file_data)

    except (FileNotFoundError, FileExistsError) as error:
        return f'File Error: {error}'

    return board_data


def save_board(filename, board):
    '''Save the current game to a file.'''

    with open(filename, 'w') as file_data:
        json.dump(board, file_data)


def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''

    # Print the grid board to the user using the data saved
    # in the JSON file.
    filler_line = '---+---+---'
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print(filler_line)
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print(filler_line)
    print(f' {board[6]} | {board[7]} | {board[8]} ')


def is_x_turn(board):
    '''Determine whose turn it is.'''
    # If there is an odd number of blank spaces left,
    # it's X's turn.
    x_counter = 0
    for square in board:
        if square == ' ':
            x_counter += 1

    if x_counter % 2 == 1:
        return True
    else:        
        return False


def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''

    # The game play is in a for loop so that it continues to run,
    # and only up to 9 times. Could also be done with a counter.
    total_spaces = 9
    for spaces_left in range(total_spaces):
        # Determine what to print to the screen depending
        # on whose turn it is.
        if is_x_turn(board) == True:
            turn = input('X>')
            new_data = 'X'
        else:
            turn = input('O>')
            new_data = 'O'

        # If the user enters 'q', save the board and end the game.
        if turn == 'q':
            board_data = {"board":board}
            save_board('Fall26_Lab01.json', board_data)
            return False

        # If the user didn't enter a 'q', turn their number into an int.
        turn = int(turn)    # could write code to catch if they didn't type a number     !!!!!!

        # Update the board data and print the updated grid to the user.
        board[turn - 1] = new_data
        display_board(board)
        # Check if the game is over, whether by a win or a tie.
        game_finished = game_done(board, message = True)

        # If the game is finished, reset the board data to be
        # an empty board and end the program.
        if game_finished == True:
            board_data = blank_board
            save_board('Fall26_Lab01.json', board_data)
            return True


def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False


if __name__ == '__main__':
    main()