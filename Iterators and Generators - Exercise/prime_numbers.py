def get_primes(list_of_integers) -> list:
    for num in list_of_integers:
        if num < 2:
            continue
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            yield num