def main():
    # sentence = "The quick brown fox jumps over the lazy dog."
    # reverse_string_loop(sentence)
    # print()
    # reverse_string_recursion(sentence)
    print(fibonacci_recursion(10))
    print(fibonacci_loop(10))


# def reverse_string_loop(sentence):
#     len_of_sent = len(sentence)

#     for i in range(len_of_sent - 1, -1, -1):
#         print(sentence[i], end='')


# def reverse_string_recursion(sentence):
#     if len(sentence) == 1:
#         print(sentence[0], end='')
#     else:
#         # if you reverse the order of these two statements, it prints the sentence forward.
#         reverse_string_recursion(sentence[1:])
#         print(sentence[0], end='')


def fibonacci_recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

def fibonacci_loop(n):
    fibonacci_data = [0] * (n + 1)
    fibonacci_data[0] = 0
    fibonacci_data[1] = 1
    for i in range(2, n + 1):
        fibonacci_data[i] = fibonacci_data[i - 1] + fibonacci_data[i - 2]
        
    return fibonacci_data[n]


main()