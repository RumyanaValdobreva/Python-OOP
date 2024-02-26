def type_check(parameter_type):
    def decorator(func):
        def wrapper(parameter):
            if not isinstance(parameter, parameter_type):
                return "Bad Type"
            return func(parameter)

        return wrapper

    return decorator