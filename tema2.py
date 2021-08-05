import decimal


def your_function(*args, **kwargs):
    sum_num: float = 0
    if args.__len__() == 0:
        return 0
    for x in args:
        if isinstance(x, (int, float, decimal.Decimal)):
            sum_num += x

    return sum_num


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))


def recursive_function(n: int):
    if n == 1:
        return 1
    else:
        return n + recursive_function(n - 1)


print(recursive_function(3))


def recursive_function_even(n: int):
    if n == 2:
        return 2
    else:
        if n % 2 == 0:
            return n + recursive_function_even(n - 1)
        else:
            return recursive_function_even(n - 1)


print(recursive_function_even(6))


def recursive_function_odd(n: int):
    if n == 1:
        return 1
    else:
        if n % 2 != 0:
            return n + recursive_function_odd(n - 1)
        else:
            return recursive_function_odd(n - 1)


print(recursive_function_odd(4))


def read_from_keyboard():
    userInput = input()
    try:
        val = int(userInput)
        return val
    except ValueError:
        return 0


print(read_from_keyboard())
