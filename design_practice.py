def main():
    test_all_conversions()
    number = get_int()
    convert_int_to_hex(10)
    binary = convert_int_to_binary(number, 2)
    convert_int_to_octal(10)
    display_nums(10, binary, 10, 10)

def get_int():
    number = -1
    while number < 0:
        try:
            number = int(input("Please input a positive integer: "))
        except (ValueError, KeyboardInterrupt, EOFError):
            print("Incorrect input.")

    return number


def convert_int_to_hex(int):
    return 0

def convert_int_to_binary(number, divisor):
    binary_digits = []
    while number > 0:
        binary_digits.append(number % divisor)
        number  = number // 2

    binary_string = ""
    for i in range(len(binary_digits) - 1, -1, -1):
        binary_string = binary_string + str(binary_digits[i])

    return binary_string

def convert_int_to_octal(int):
    return 0

def display_nums(dec, bin, hex, oct):
    print("Here are the conversions of your number:")
    print(f"Decimal: {dec}")
    print(f"Binary: {bin}")
    print(f"Hexadecimal: {hex}")
    print(f"Octal: {oct}")

def test_all_conversions():
    test_convert_int_to_binary()

def test_convert_int_to_hex():
    pass

def test_convert_int_to_binary():
    assert convert_int_to_binary(0, 2) == ''
    assert convert_int_to_binary(1, 2) == '1'
    assert convert_int_to_binary(2, 2) == '10'
    assert convert_int_to_binary(10, 2) == '1010'
    assert convert_int_to_binary(31, 2) == '11111'
    assert convert_int_to_binary(127, 2) == '1111111'
    assert convert_int_to_binary(128, 2) == '10000000'
    assert convert_int_to_binary(255, 2) == '11111111'
    assert convert_int_to_binary(256, 2) == '100000000'

def test_convert_int_to_octal():
    pass

main()