class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = tuple(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dictionary):
            index = self.index
            self.index += 1
            return self.dictionary[index]
        else:
            raise StopIteration()