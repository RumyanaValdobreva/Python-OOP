class reverse_iter:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.current_index = len(self.iterable_object) - 1
        self.end_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index -= 1
        return self.iterable_object[index]