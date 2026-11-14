# 1. Name:
#      Alayna Earl
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program takes a list (of typically numbers) and sorts them
#      by sorting with sublists. Then it prints the sorted list to
#      the screen.
# 4. What was the hardest part? Be as specific as possible.
#      My code was poorly written and overly complicated from
#      the start. I had so many little errors, including off by one
#      errors. What took me the longest was going through with the
#      debugger to get to the point that was broken.
# 5. How long did it take for you to complete the assignment?
#      270 minutes

def main():
    """
    This program takes a list and sorts it.
    """
    test_driver()
    current_list = [12, 10, 11, 8, -1, 16, 2, 20, 11, 3, 4, 1]
    get_sorted_list(current_list)
    print("Here is the sorted list:")
    print(current_list)


def get_sorted_list(current_list):
    """
    This function takes in an unsorted list and sorts it with the help
    of two other functions. It doesn't return anything, because lists
    pass by reference. 
    This function sets a destination list that is the same length as
    the original to use as a temp list while sorting. It uses two while
    loops, one that goes while the list is not sorted, and one that
    goes until all of the sublists have been found in that pass
    through.
    After each pass, it updates the part of the current list
    to match the part that has been sorted in the destination list.
    """
    list_length = len(current_list)
    destination_list = [0] * list_length
    if list_length > 1:
        is_sorted = False
        while not is_sorted:
            sublist1_start = 0
            all_sublists_found = False
            number_of_times_through = 0
            while not all_sublists_found:
                sublist1_end, sublist2_end = get_two_sublists_indexes(sublist1_start, current_list)
                if sublist2_end == 0:
                    all_sublists_found = True
                if all_sublists_found and (number_of_times_through == 0 or list_length == 2):
                    is_sorted = True

                if not is_sorted:
                    merge_two_sublists(current_list, destination_list, sublist1_start, sublist1_end, sublist2_end)

                    if sublist2_end != list_length - 1:
                        sublist1_start = sublist2_end + 1
                        number_of_times_through += 1
                    else:
                        all_sublists_found = True

                    dest_index = max(sublist1_end, sublist2_end)
                    for i in range(dest_index + 1):
                        current_list[i] = destination_list[i]

    elif list_length == 1:
        destination_list[0] = current_list[0]


def get_two_sublists_indexes(sublist1_start, list):
    """
    This function takes in an integer representing the index of the
    start of a sublist and a list. It returns a tuple containing two
    integers, which are the indexes for the end of one sublist and
    the end of the proceeding sublist.
    """
    sublist1_end = sublist1_start
    sublist2_end = 0
    sublists_found = 0

    while sublists_found < 2 and sublist1_end < len(list) - 1 and sublist2_end < len(list) - 1:
        for i in range(sublist1_end + 1, len(list)):
            if sublists_found == 0:
                if list[i] >= list[sublist1_end]:
                    sublist1_end += 1
                elif list[i] < list[sublist1_end]:
                    sublist2_end = i
                    sublists_found += 1
            elif sublists_found == 1:
                if list[i] >= list[sublist2_end]:
                    sublist2_end += 1
                elif list[i] < list[sublist2_end]:
                    sublists_found += 1

        if sublist1_end == len(list):
            sublist1_end -= 1
        if sublist2_end == len(list):
            sublist2_end -= 1

    return sublist1_end, sublist2_end


def merge_two_sublists(list, dest_list, sublist1_start, sublist1_end, sublist2_end):
    """
    This function takes in the list to be sorted and the temporary list
    to sort to. It also takes in the indexes for the start and end of
    the first sublist, as well as the end index of the second sublist.
    It does not return anything, because it is updating the temporary
    list, which is passed by reference.
    """
    if sublist2_end > 0:
        sublist2_start = sublist1_end + 1
    else:
        sublist2_start = 0

    final_sublist = 0
    dest_index = sublist1_start

    if len(list) >= 2:
        if sublist2_end == 0 or list[sublist1_end] > list[sublist2_end]:
            final_sublist = 1
        elif list[sublist1_end] <= list[sublist2_end] and sublist2_end != 0:
            final_sublist = 2

        while sublist1_start <= sublist1_end and sublist2_start <= sublist2_end and sublist2_end != 0:
            if list[sublist1_start] <= list[sublist2_start]:
                dest_list[dest_index] = list[sublist1_start]
                sublist1_start += 1
            else:
                dest_list[dest_index] = list[sublist2_start]
                sublist2_start += 1
            dest_index += 1

    if final_sublist == 1:
        for i in range(sublist1_start, sublist1_end + 1):
            dest_list[dest_index] = list[i]
            dest_index += 1
    elif final_sublist == 2:
        for i in range(sublist2_start, sublist2_end + 1):
            dest_list[dest_index] = list[i]
            dest_index += 1


def test_driver():
    test_get_sorted_list()
    test_get_two_sublists_indexes()
    test_merge_two_sublists()

# These test functions test each function based on the
# following test cases: Empty list, list with a length of
# 1, an unsorted list of length two, a list of duplicates,
# a medium sized list, and a larger list. For the main
# sorting function, it also tests a few error cases where
# the input is something other than a list. The main one
# also tests an already sorted small list.

def test_get_sorted_list():
    list = []
    get_sorted_list(list)
    assert list == []

    list = [0]
    get_sorted_list(list)
    assert list == [0]

    list = [2, 1]
    get_sorted_list(list)
    assert list == [1, 2]

    list = [1, 2, 3, 4]
    get_sorted_list(list)
    assert list == [1, 2, 3, 4]

    list = [3, 3, 3, 3]
    get_sorted_list(list)
    assert list == [3, 3, 3, 3]

    list = [1, -2, 4, 3, 10, 6, 8, 6]
    get_sorted_list(list)
    assert list == [-2, 1, 3, 4, 6, 6, 8, 10]

    list = [12, 10, 11, 8, -1, 16, 2, 20, 11, 3, 4, 1]
    get_sorted_list(list)
    assert list == [-1, 1, 2, 3, 4, 8, 10, 11, 11, 12, 16, 20]

    # list = 0
    # get_sorted_list(list)
    # # Should fail and show a TypeError

    # list = False
    # get_sorted_list(list)
    # # Should fail and show a TypeError

    # list = "unsorted string"
    # get_sorted_list(list)
    # # Should fail and show a TypeError


def test_get_two_sublists_indexes():
    assert get_two_sublists_indexes(0, []) == (0, 0)
    assert get_two_sublists_indexes(0, [0]) == (0, 0)
    assert get_two_sublists_indexes(0, [2, 1]) == (0, 1)
    assert get_two_sublists_indexes(0, [3, 3, 3, 3]) == (3, 0)
    assert get_two_sublists_indexes(0, [1, -2, 4, 3, 10, 6, 8, 6]) == (0, 2)
    assert get_two_sublists_indexes(0, [12, 10, 11, 8, -1, 16, 2, 20, 11, 3, 4, 1]) == (0, 2)

    assert get_two_sublists_indexes(3, [-2, 1, 4, 3, 10, 6, 8, 6]) == (4, 6)
    assert get_two_sublists_indexes(3, [10, 11, 12, 8, -1, 16, 2, 20, 11, 3, 4, 1]) == (3, 5)


def test_merge_two_sublists():
    list = []
    dest_list = []
    merge_two_sublists(list, dest_list, 0, 0, 0)
    assert dest_list == []

    list = [0]
    dest_list = [0]
    merge_two_sublists(list, dest_list, 0, 0, 0)
    assert dest_list == [0]

    list = [2, 1]
    dest_list = [0, 0]
    merge_two_sublists(list, dest_list, 0, 0, 1)
    assert dest_list == [1, 2]

    list = [3, 3, 3, 3]
    dest_list = [0, 0, 0, 0]
    merge_two_sublists(list, dest_list, 0, 3, 0)
    assert dest_list == [3, 3, 3, 3]

    list = [1, -2, 4, 3, 10, 6, 8, 6]
    dest_list = [0, 0, 0, 0, 0, 0, 0, 0]
    merge_two_sublists(list, dest_list, 0, 0, 2)
    assert dest_list == [-2, 1, 4, 0, 0, 0, 0, 0]

    list = [12, 10, 11, 8, -1, 16, 2, 20, 11, 3, 4, 1]
    dest_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    merge_two_sublists(list, dest_list, 0, 0, 2)
    assert dest_list == [10, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0]


if __name__ == "__main__":
    main()