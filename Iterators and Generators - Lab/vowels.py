class vowels:
    def __init__(self, string: str):
        self.string = string
        vowels_ = ["a", "i", "e", "u", "y", "o"]
        self.found_vowels = [el for el in self.string if el.lower() in vowels_]
        self.current_index = 0
        self.end_index = len(self.found_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration()
        index = self.current_index
        self.current_index += 1
        return self.found_vowels[index]