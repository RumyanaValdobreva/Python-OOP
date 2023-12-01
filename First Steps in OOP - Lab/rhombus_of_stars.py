def print_row(number, row):
    print(" " * (number - row), end="")
    print(*["*"] * row)


def upper_part(number):
    for row in range(1, number + 1):
        print_row(number, row)


def bottom_part(number):
    for row in range(number - 1, 0, -1):
        print_row(number, row)


def result(number):
    upper_part(number)
    bottom_part(number)


number = int(input())

result(number)
