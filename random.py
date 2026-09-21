# def determine_title(gender):
#     if gender == 'm':
#         return 'Mr.'
#     else:
#         return 'Ms.'

# last_name = input('What is your last name? ')
# gender = input('Are you male or female (m/f)? ').lower()
# title = determine_title(gender)
# print(f'Hello, {title} {last_name}.')

# def get_age(birth_year):
#     return 2026 - birth_year

# birth_year = int(input('What year were you born? '))
# age = get_age(birth_year)
# print(f'You will turn {age} this year.')



# import json

# def write_data_to_json_file(file_name, data):
#     try:
#         with open(file_name, 'wt') as file_handle:
#             # json.dump(data, file_handle)
#             # the above is the same as the next two lines
#             json_data = json.dumps(data) # dumps = dump string
#             file_handle.write(json_data)

#     except (FileExistsError, FileNotFoundError) as error:
#         print(f'File Error: {error}')

# def read_data_from_json_file(file_name):
#     try:
#         with open(file_name, 'rt') as file_handle:
#             file_data = json.load(file_handle)
#         return file_data

#     except (FileNotFoundError, FileExistsError) as error:
#         print(f'File Error: {error}')

# def main():

#     file_name = 'my_friends2.json'

#     my_friends = {
#         'names' : ['Bob', 'Jane', 'Opal'],
#         'phone_numbers' : [2081234567, 2088675309, 1343452131],
#         'ages' : [34, 52, 14],
#         'owes_me' : [14.32, 500.32, 4.10]
#     }

#     # print(my_friends['names'])
#     write_data_to_json_file(file_name, my_friends)

#     friend_data = read_data_from_json_file('my_friends2.json')
#     print(friend_data)


# if __name__ == '__main__':
#     main()
