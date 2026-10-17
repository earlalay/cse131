# 1. Name:
#      Alayna Earl
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

# 90 minutes
# 11:53
# everything but the two hint ones

from pathlib import Path

def main():
    print("to make the file happy")


def get_starting_filename():
    """
    Get the filename for the starting board from the user.
    """
    print("Enter the file for the game you want to start.")
    print("It needs to end in '.json'.", end=" ")

    valid_file = False
    while not valid_file:
        filename = input("Filename: ", end="")
        
        if not is_file_type_JSON(filename):
            print("Invalid file type. Please try again.")

        elif not Path(filename).is_file():
            print("File not found. Please try again.")

        else:
            valid_file = True


def is_file_type_JSON(filename):
    """
    Return a boolean indicating if the last five characters of the
    filename provided by the user are '.json'.
    """
    if filename[-5:] == ".json":
            return True
    else:
        return False


def get_board_from_file(file):
    """
    Return a variable containing the JSON object that is the
    beginning sudoku board from the provided JSON file.
    """


def display_board(board):
    """
    Print the current sudoku board to the user.
    """
    print("   A B C D E F G H I")
    for row in range(9):
        print(f"{row + 1}   ")
        if row == 3 or row == 6:
            print("---+---+---")
        else:
            for column in range(9):
                separator = "   |   |   \n"
                if board[column][row] == 0:
                    print(" ")
                else:
                    print(board[column][row])

                print(separator[column])


def give_hint(coordinate):
    """
    Provide the user with a list of possible numbers for the
    chosen coordinate (could include incorrect answers).
    """


def compute_valid_num_list(coordinate):
    """
    Create a list of possible numbers at the given coordinate. Do so
    by comparing the available numbers in the corresponding row,
    column, and 3x3 cell.
    """


def get_num_entry():
    """
    Ask the user for the number they would like to enter for their
    chosen coordinate. It will be verified in other functions.
    """
    print("Please enter a number for your chosen coordinate (1-9).", end=" ")
    valid_num = False
    while not valid_num:
        number = input("Number: ", end="")

        if not is_valid_int(number):
            print("That isn't in range. Please try again.")
        else:
            number = int(number)
            valid_num = True

    return number


def is_num_available(board, target_row, target_col, number):
    """
    Return a boolean indicating if the number the user would like
    to enter does not occur in the corresponding row, column,
    and 3x3 cell.
    """
    for col_num in board[target_row]:
        if col_num == number:
            return False

    for row_num in range(9):
        if board[row_num][target_col] == number:
            return False

    starting_row = target_row // 3 * 3
    starting_col = target_col // 3 * 3
    for row in range(starting_row, starting_row + 3):
        for col in range(starting_col, starting_col + 3):
            if board[row][col] == number:
                return False


def is_valid_int(num_entry_input):
    """
    Return a boolean indicating if the number the user would like
    to enter is a number in the range 1-9.
    """
    valid_inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if num_entry_input in valid_inputs:
        return True
    else:
        return False


def get_coordinate():
    """
    Get the coordinate from the user that they would like to enter
    a number in. The validity and availability of the coordinate
    will be checked in other functions.
    """


def is_valid_coord(coord_input):
    """
    Return a boolean indicating if the user's coordinate is valid.
    It should only be two characters, comprised of one letter and
    one number. The number needs to be in the range 1-9 and the
    letter needs to be in the range A-I.
    """


def is_coord_free(coord_input):
    """
    Return a boolean indicating if the inputed coordinate is free,
    meaning that it does not already have a number there.
    """


def get_indexes_from_coord(coordinate):
    """
    Convert and return the provided coordinate (containing a letter
    and a number) to a tuple containing what will be two indexes.
    """
    row_dict = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4,
                '6': 5, '7': 6, '8': 7, '9': 8}
    col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                'F': 5, 'G': 6, 'H': 7, 'I': 8}
    row_key = coordinate[1]
    col_key = coordinate[0]
    row_value = row_dict[row_key]
    col_value = col_dict[col_key]
    coord_indexes = (row_value, col_value)
    return coord_indexes


def save_game(board):
    """
    Save the game board to a file. Get the file to save to from another
    function that gets the filename from the user.
    """


def get_save_filename():
    """
    Get and return a filename from the user corresponding what
    file they want to save their game to. Confirm its validity
    with other functions.
    """


def is_save_file_template(filename):
    """
    Return a boolean indicating if the given filename corresponds to
    the default game boards that should not be saved to.
    """


if __name__ == "__main__":
    main()