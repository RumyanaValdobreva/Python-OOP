def read_next(*args):
    for collection in args:
        for element in collection:
            yield element