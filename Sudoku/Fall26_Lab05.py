# 1. Name:
#      Alayna Earl
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This program allows the user to play sudoku.
# 4. What was the hardest part? Be as specific as possible.
#      Just managing how many moving parts there are. Lots can and did go wrong.
# 5. How long did it take for you to complete the assignment?
#      Draft - 325 minutes
#      Final version - 110 minutes


import json
from pathlib import Path

def main():
    print("Welcome to Sudoku!")
    print(
        "When you enter a coordinate, it should include a letter " +
        "and a number."
    )
    print(
        "For example, A1 or 1A. Both upper and lowercase letters " +
        "will work."
    )

    starting_file = get_starting_filename()
    board = get_board_from_file(starting_file)
    indexed_coord = ()

    game_over = False
    while not game_over:
        display_board(board)
        user_move = get_valid_move(board)
        if len(user_move) == 1:
            game_over = True
            if is_saving_game():
                save_filename = get_save_filename()
                save_game(board, save_filename)            
        else:
            indexed_coord = get_indexes_from_coord(user_move)
            row = indexed_coord[0]
            col = indexed_coord[1]

            hint_wanted = wants_hint()
            if hint_wanted:
                valid_num_list = compute_valid_num_list(board, row, col)
                give_hint(user_move, valid_num_list)
            else:
                valid_number_value = False
                while not valid_number_value:
                    number_value = get_num_entry()
                    if is_num_available(board, row, col, number_value) == "num_in_row":
                        print("That number is already in that row.")
                    elif is_num_available(board, row, col, number_value) == "num_in_col":
                        print("That number is already in that column.")
                    elif is_num_available(board, row, col, number_value) == "num_in_cell":
                        print("That number is already in that cell.")
                    elif is_num_available(board, row, col, number_value) == "num_available":
                        board[row][col] = number_value
                        valid_number_value = True
                    else:
                        print("Something went wrong.")


def get_starting_filename():
    """
    Get the filename for the starting board from the user.
    """
    print("Enter the file for the game you want to start.")
    print("It needs to end in '.json'.", end=" ")

    valid_file = False
    while not valid_file:
        filename = input("Filename: ")
        
        if not is_file_type_JSON(filename):
            print("Invalid file type. Please try again.")

        elif not (Path(__file__).parent / filename).is_file():
            print("File not found. Please try again.")

        else:
            valid_file = True
    return Path(__file__).parent / filename


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
    with open(file, 'r') as game_file:
        raw_json_data = game_file.read()

    board = json.loads(raw_json_data)
    return board["board"]


def display_board(board):
    """
    Print the current sudoku board to the user.
    """
    print("    A B C D E F G H I")
    row_count = 1
    for row in range(9):
        print(f"{row_count}   ", end="")
        for column in range(9):
            if board[row][column] == 0:
                print(" ", end="|" if column in [2, 5] else " ")
            else:
                print(board[row][column], end="|" if column in [2, 5] else " ")

            if column == 8:
                print()

        if row_count == 3 or row_count == 6:
            print("    -----+-----+-----")

        row_count += 1


def wants_hint():
    """
    If the user selects a coordinate, this function asks if they want
    a hint or if they want to enter a number. If they want a hint,
    it returns True. If they want to enter a number, it returns False.
    """
    valid_input = False
    while not valid_input:
        user_move = input("If you want a hint for your coordinate, type 'H'. " + 
                        "If you want to enter a number, type 'N': ")
        if user_move.lower() != 'h' and user_move.lower() != 'n':
            print("Invalid input.")
        else:
            valid_input = True

    if user_move.lower() == 'h':
        return True
    elif user_move.lower() == 'n':
        return False


def give_hint(coordinate, valid_num_list):
    """
    Provide the user with a list of possible numbers for
    the chosen coordinate's row and column (could include
    incorrect answers).
    """
    print(f"The available numbers for {coordinate} are {str(valid_num_list)[1:-1]}.")


def compute_valid_num_list(board, target_row, target_col):
    """
    Create a list of possible numbers at the given coordinate. Do so
    by comparing the available numbers in the corresponding row,
    column, and 3x3 cell.
    """
    valid_num_list = []
    for num in range (1, 10):
        col_counter = -1
        cell_counter = -1
        for col_num in board[target_row]:
            row_counter = 0
            if col_num == num:
                row_counter += 1
        if row_counter == 0:
            for row_num in range(9):
                col_counter = 0
                if board[row_num][target_col] == num:
                    col_counter += 1
        if col_counter == 0:
            cell_counter = 0
            starting_row = target_row // 3 * 3
            starting_col = target_col // 3 * 3
            for row in range(starting_row, starting_row + 3):
                for col in range(starting_col, starting_col + 3):
                    if board[row][col] == num:
                        cell_counter += 1
        if cell_counter == 0:
            valid_num_list.append(num)

    return valid_num_list

def get_num_entry():
    """
    Ask the user for the number they would like to enter for their
    chosen coordinate. It will be verified in other functions.
    """
    print("Please enter a number for your chosen coordinate (1-9).")
    valid_num = False
    while not valid_num:
        number = input("Number: ")

        if not is_valid_int(number):
            print("That isn't in range. Please try again.")
        else:
            number = int(number)
            valid_num = True

    return number


def is_num_available(board, target_row, target_col, number):
    """
    Check if the number the user would like to enter occurs in
    the corresponding row, column, and 3x3 cell. Return a string
    indicating if the number if available, or where it already is.
    """
    for col_num in board[target_row]:
        if col_num == number:
            return "num_in_row"

    for row_num in range(9):
        if board[row_num][target_col] == number:
            return "num_in_col"

    starting_row = target_row // 3 * 3
    starting_col = target_col // 3 * 3
    for row in range(starting_row, starting_row + 3):
        for col in range(starting_col, starting_col + 3):
            if board[row][col] == number:
                return "num_in_cell"
    return "num_available"


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


def get_valid_move(board):
    """
    Get the next move the user would like to do. They include entering
    a coordinate or 'Q' to quit.
    Returns a coordinate or the letter Q upper or lower case.
    """
    valid_move = False
    while not valid_move:
        user_input = input(
                           "Specify a coordinate to edit or 'Q' to quit " +
                           "(with the option to save): "
                        )

        if len(user_input) == 1:
            if user_input != 'Q' and user_input != 'q':
                print("Invalid choice.")
            else:
                valid_move = True

        elif len(user_input) == 2:
            if not is_valid_coord(user_input):
                print("Invalid coordinate.")
            else:
                indexed_coord = get_indexes_from_coord(user_input)
                if not is_coord_free(board, indexed_coord):
                    print("That place already has a number.")
                else:
                    valid_move = True
        else:
            print("Incorrect number of characters.")

    return user_input


def is_valid_coord(coord):
    """
    Return a boolean indicating if the user's coordinate is valid.
    It should only be two characters, comprised of one letter and
    one number. The number needs to be in the range 1-9 and the
    letter needs to be in the range A-I.
    """
    valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid_letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e',
                     'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i']
    number_count = 0
    letter_count = 0
    for i in range(2):
        if coord[i] not in valid_numbers and coord[i] not in valid_letters:
            return False
        elif coord[i] in valid_numbers:
            number_count += 1
        else:
            letter_count += 1

    if number_count == 2 or letter_count == 2:
        return False

    return True


def is_coord_free(board, indexed_coord):
    """
    Return a boolean indicating if the inputed coordinate is free,
    meaning that it does not already have a number there.
    """
    row = indexed_coord[0]
    col = indexed_coord[1]
    if board[row][col] == 0:
        return True
    else:
        return False


def get_indexes_from_coord(coordinate):
    """
    Convert and return the provided coordinate (containing a letter
    and a number) to a tuple containing what will be two indexes.
    """
    valid_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    row_dict = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4,
                '6': 5, '7': 6, '8': 7, '9': 8}
    col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
                'F': 5, 'G': 6, 'H': 7, 'I': 8}

    if coordinate[0] in valid_numbers:
        uppercase_letter = coordinate[1].upper()
        formatted_coord = f"{coordinate[0]}{uppercase_letter}"
    else:
        uppercase_letter = coordinate[0].upper()
        formatted_coord = f"{coordinate[1]}{uppercase_letter}"
    
    row_key = formatted_coord[0]
    col_key = formatted_coord[1]
    row_value = row_dict[row_key]
    col_value = col_dict[col_key]
    coord_indexes = (row_value, col_value)
    return coord_indexes


def is_saving_game():
    """
    Gets and returns a yes or a no from the user indicating if
    they want to save their game.
    """
    print("Do you want to save your game?", end=" ")
    while True:
        save_game = input("Yes or no: ").lower()
        if save_game == "yes":
            return True
        elif save_game == "no":
            return False
        else:
            print("Invalid option.")


def save_game(board, filename):
    """
    Save the game board to a file with the provided filename.
    """
    file_path = Path(__file__).parent / filename

    with open(file_path, 'w') as file:
        json.dump({"board": board}, file)


def get_save_filename():
    """
    Get and return a filename from the user corresponding what
    file they want to save their game to. Confirm its validity
    with other functions.
    """
    print("Enter the file you want to save the game to.")
    print("It needs to end in '.json'.")

    valid_file = False
    while not valid_file:
        filename = input("Filename: ")
        
        if not is_file_type_JSON(filename):
            print("Invalid file type. Please try again.")

        elif is_save_file_template(filename):
            print("You can't save to the original game file.")

        else:
            valid_file = True
    return filename


def is_save_file_template(filename):
    """
    Return a boolean indicating if the given filename corresponds to
    the default game boards that should not be saved to.
    """
    easy_game_template = "131.05.Easy.json"
    medium_game_template = "131.05.Medium.json"
    hard_game_template = "131.05.Hard.json"

    if filename == easy_game_template:
        return True
    elif filename == medium_game_template:
        return True
    elif filename == hard_game_template:
        return True
    else:
        return False


if __name__ == "__main__":
    main()