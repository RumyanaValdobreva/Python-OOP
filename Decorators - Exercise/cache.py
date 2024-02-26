def cache(func):
    def wrapper(number):
        if not wrapper.log.get(number):
            wrapper.log[number] = func(number)
        return wrapper.log[number]

    wrapper.log = {}
    return wrapper