def even_numbers(function):
    def wrapper(numbers):
        even_numbers = [n for n in numbers if n % 2 == 0]
        return function(even_numbers)
    return wrapper


# def even_numbers(function):
#     def wrapper(numbers):
#         even_numbers = [n for n in numbers if n % 2 == 0]
#         return even_numbers
#     return wrapper