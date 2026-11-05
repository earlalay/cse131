# This file is for practicing watching the callstack while debugging.
# It practices recursion to also watch the callstack.


# def main():
#     a = 10
#     total = function_1(a)
#     print(total)

# def function_1(x):
#     x += function_2(x)
#     return x

# def function_2(y):
#     y += 20
#     return y

# main()


def main():
    factorial = 5
    factored = factorial_loop(factorial)
    print(factored)
    recursion_factorial = factorial_recursion(factorial)
    print(recursion_factorial)

def factorial_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def factorial_recursion(n):
    # Could be n == 0 or n <= 1. But n == 1 makes the most sense.
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

main()