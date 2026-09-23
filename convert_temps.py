# unfinished

def main():
    print("instructions")
    temp = get_temp()
    temp_type = get_temp_type()

    # make it lowercase
    if temp_type == "f":
        
    elif temp_type == "c":

    else:


def get_temp():
    valid_temp = False
    while not valid_temp:
        temp = input('What is the temperature? ')
        if validate_num_char:
            return temp
        else:
            print('Invalid temperature.')


def validate_num_char(temp):
    # Make a list of all the valid characters for an input of a number.
    num_char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Assert the length of num_char_list is 10, one for each number char.
    assert len(num_char_list) == 10
    # Make a variable that will keep track of whether or not there are
    # invalid characters in the number input.
    bad_char_counter = 0
    # Assert bad_char_counter starts at 0.
    assert bad_char_counter == 0
    # Loop through each character of the user's input.
    for character in temp:
        # If the character is invalid, increase the counter.
        if character not in num_char_list:
            bad_char_counter += 1
    # Assert bad_char_counter is not a negative number.
    assert bad_char_counter > -1
    # If there is at least one invalid character, return False.
    if bad_char_counter > 0:
        return False
    # Else, return True to signify that it is a valid input
    # in regards to it being a number.
    else:
        return True


def get_temp_type():
    valid_temp_type = False
    while not valid_temp_type:
        temp_type = input('What is the temperature type? ')
        if validate_char:
            return temp_type
        else:
            print('Invalid temperature type.')


def validate_char(temp_type):
    valid_temp_type = ['F', 'C', 'K', 'f', 'c', 'k']
    if temp_type not in valid_temp_type:
        return False
    else:
        return True


def convert_to_celsius(temp):



def convert_to_fahrenheit(temp):



def convert_to_kelvin(temp):



def print_temps(f, c, k):
    print(f'Temperature in Fahrenheit: {f}')
    print(f'Temperature in Celsius: {c}')
    print(f'Temperature in Kelvin: {k}')