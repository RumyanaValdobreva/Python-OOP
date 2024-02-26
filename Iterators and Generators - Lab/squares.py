def squares(n):
    start_num = 1
    while start_num <= n:
        yield start_num * start_num
        start_num += 1