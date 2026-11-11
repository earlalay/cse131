# 1. Name:
#      Alayna Earl
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      35 minutes

def main():
    current_list = [2, 1]
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
                        is_sorted = True

                    current_list, destination_list = destination_list, current_list
    elif list_length == 1:
        destination_list[0] = current_list[0]

    print(current_list)


def get_two_sublists_indexes(sublist1_start, list):
    sublist1_end = sublist1_start
    sublist2_end = 0
    sublists_found = 0

    while sublists_found < 2 and sublist1_end < len(list) - 1 and sublist2_end < len(list) - 1:
        for i in range(sublist1_start + 1, len(list)):
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
    if sublist2_end > 0:
        sublist2_start = sublist1_end + 1
    else:
        sublist2_start = 0

    sublist1_range = sublist1_end - sublist1_start + 1
    sublist2_range = sublist2_end - sublist2_start + 1
    dest_index = sublist1_start

    if sublist1_range > sublist2_range:
        larger_sublist = 1
    elif sublist1_range < sublist2_range:
        larger_sublist = 2

    while (sublist1_start <= sublist1_end or sublist2_start <= sublist2_end) and len(list) >= 2:
        if list[sublist1_start] <= list[sublist2_start]:
            dest_list[dest_index] = list[sublist1_start]
            sublist1_start += 1
        else:
            dest_list[dest_index] = list[sublist2_start]
            sublist2_start += 1
        dest_index += 1

    if larger_sublist == 1 and sublist2_end != 0:
        for i in range(sublist1_start, sublist1_range):
            dest_list[i] = list[i]
    elif larger_sublist == 2:
        for i in range(sublist2_start, sublist2_range):
            dest_list[i] = list[i]

if __name__ == "__main__":
    main()