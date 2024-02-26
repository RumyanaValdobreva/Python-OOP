def genrange(start: int, end: int):
    current = start
    while current <= end:
        yield current
        current += 1

# def genrange(start: int, end: int):
#     for i in range(start, end + 1):
#         yield i