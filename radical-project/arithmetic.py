def add_two_numbers(a, b):
    return a + b


def add_three_numbers(a, b, c) -> int:
    return a + b + c

def uppercase_word(word: str) -> str:
    return word.upper()

def add_any_numbers(*a):
    sum_ = 0
    for num in a:
        sum_ += num
    return sum_

