def even_parameters(function):
    def wrapper(*args):
        for param in args:
            if not isinstance(param, int) or param % 2 != 0:
                return "Please use only even numbers!"
        return function(*args)

    return wrapper