# 1. Name:
#      Alayna Earl
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program takes a month and a year (after 1752) from the 
#      user and prints the calendar for that month to the user.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was being careful when encountering all
#      of the common off-by-1 errors. I mostly encountered it when
#      setting ranges.
# 5. How long did it take for you to complete the assignment?
#      110 minutes


def main():
    # Get the month for the calendar and the year it's in.
    month = get_month()
    year = get_year()

    # Get the number of days in the month, accounting for 
    # Februarys in leap years.
    if month != 2:
        days_in_month = get_days_in_month(month)
    else:
        days_in_month = get_days_in_month(month, year)

    # Create a list to hold True or False for each year between
    # the starting and ending years being leap years.
    is_leap_year_list = []

    # Asserts is_leap_year_list is the type 'list'.
    assert type(is_leap_year_list) == list
    # Check if each year between the starting and ending years
    # are leap years and add that date to is_leap_year_list
    # by using the is_leap_year function.
    for year in range(1753, year + 1):
        leap_year_check = is_leap_year(year)
        is_leap_year_list.append(leap_year_check)

    # Get the number of days in the year prior to the indicated month.
    # Do this by looping through the range of months prior.
    days_in_months_prior = 0
    for month in range (1, month + 1):
        days_in_months_prior += get_days_in_month(month, year)

    # The offset is to tell the program how many spaces to put before
    # printing the first day in the calendar.
    offset = compute_offset(month, year)

    display_table(offset, days_in_month)


def get_month():
    # Set valid_month to False to enter the while loop.
    valid_month = False
    # Assert valid_month is False in order to enter the while loop.
    assert valid_month == False
    # Keep asking the user to enter a month until they
    # enter a valid input (only number characters).
    while not valid_month:
        month = input("Enter the month number: ")
        valid_month = check_char_in_number(month)
        # Assert that valid_month is still type 'bool'.
        assert type(valid_month) == bool
        if valid_month:
            # If the month is only valid characters, turn
            # it into an integer.
            month = int(month)
            # Assert year is type 'int'.
            assert type(month) == int
            # If the month is not in the range 1-12, tell the user
            # that it isn't a valid month and have them try again.
            if month <= 0 or month > 12:
                print('Month out of range.')
                valid_month = False
        # If the user enters invalid characters, tell them to
        # only enter numbers and have them try again.
        else:
            # Assert valid_year is False in this else statement.
            assert valid_month == False
            print('Please only enter numbers.')
    # Once the user has entered a valid month made up of number
    # characters and in the range 1-12, return the month.
    return month


def get_year():
    # Set valid_year to False to enter the while loop.
    valid_year = False
    # Assert valid_year is False in order to enter the while loop.
    assert valid_year == False
    # Keep asking the user to enter a year until they
    # enter a valid input (only number characters).
    while not valid_year:
        year = input("Enter year: ")
        valid_year = check_char_in_number(year)
        # Assert that valid_year is still type 'bool'.
        assert type(valid_year) == bool
        if valid_year:
            # If the year is only valid characters, turn it
            # into an integer.
            year = int(year)
            # Assert year is type 'int'.
            assert type(year) == int
            # If the year <= 1752, turn it invalid and
            # tell the user, because this program can't handle that.
            if year <= 1752:
                print('Please enter a later year.')
                valid_year = False
        # If the user enters invalid characters, tell them to
        # only enter numbers and have them try again.
        else:
            # Assert valid_year is False in this else statement.
            assert valid_year == False
            print('Please only enter numbers.')
    # Once the user has entered a valid year made up of number
    # characters and after the year 1752, return the year.
    return year


def check_char_in_number(number):
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
    for character in number:
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


def get_days_in_month(month, year=None):
    # Make a dictionary with keys that represent the months of the year
    # and the values hold the number of days in that month.
    day_per_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                     7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # Assert that the length of day_per_month is 12, one
    # key-value pair for each month of the year.
    assert len(day_per_month) == 12

    # Access the days in the designated month via the dictionary.
    days_in_month = day_per_month[month]

    # If the month if February and the year is a leap year,
    # add an extra day.
    if month == 2 and is_leap_year(year):
        days_in_month += 1
    
    return days_in_month


def is_leap_year(year):
    # Check if the year passed to the function is a leap year or not.
    # Return True if it is a leap year and False if it isn't.
    # Check if the year is divisibe by 4.
    if year % 4 != 0:
        # If it isn't divisible by 4, return False.
        return False
    # Assert year is evenly divisible by 4 here if it gets here.
    assert year % 4 == 0
    # If the year is divisible by 4, check if it is divisible by 100.
    if year % 100 != 0:
        # If it is divisible by 4 and not 100, return True.
        return True
    # Assert year is evenly divisible by 100 here if it gets here.
    assert year % 100 == 0
    # If it is divisible by both 4 and 100, check if it is
    # divisible by 400.
    if year % 400 == 0:
        # If it is divisible by 4, 100, and 400, return True.
        return True
    else:
        # Assert year is not evenly divisble by 400 if it gets here.
        assert year % 400 != 0
        # If it divisible by 4 and 100, but not 400, return False.
        return False


def get_days_in_years(leap_year_TF_list):
    # Get the number of days in a passed list of years.
    # The list holds True and False values.
    # Start the day counter at 0.
    days_in_years = 0
    # Assert the days_in_years counter starts at 0.
    assert days_in_years == 0
    # Loop through each year in the passed list.
    for is_leap_year in leap_year_TF_list:
        # If the value in the list is True, add 366
        # to the day counter.
        if is_leap_year:
            days_in_years += 366
        # If the value in the list is False, add 365
        # to the day counter.
        else:
            # Assert is_leap_year is False here.
            assert is_leap_year == False
            days_in_years += 365
    # Return the number of days in the list of years.
    return days_in_years


def compute_offset(month, year):
    # Count the numb of days in the years prior to the specified year.
    # Do this by looping through the years and adding each set of days.
    num_days = 0
    for year_count in range(1753, year):
        if is_leap_year(year_count):
            num_days += 366
        else:
            num_days += 365

    # Count the number of days in the months prior to the specified
    # month. Do this by looping through the months and adding each
    # set of days to the days in the years prior.
    for month_count in range(1, month):
        num_days += get_days_in_month(month_count, year)

    # The first day we are calculating from is a Monday, so we
    # add 1 to the number of days before getting the remainder
    # from dividing by 7.
    return (num_days + 1) % 7


def display_table(dow, num_days):
    # Confirm that the data passed into the function are ints.
    assert(type(num_days) == type(dow) == type(0))
    # Confirm that the offset passed in is between 1 and 6.
    assert(0 <= dow <= 6)
    # Confirm that the number of days passed in for the month are
    # between 28 and 31.
    assert(28 <= num_days <= 31)

    # Display a table header containing the 7 days of the week.
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week.
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


# Run the program when this file is run.
if __name__ == "__main__":
    main()