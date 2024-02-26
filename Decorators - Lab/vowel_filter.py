def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels = ["a", "o", "e", "i", "u", "y"]
        result = [el for el in letters if el.lower() in vowels]
        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


# def vowel_filter(function):
#     def wrapper():
#         letters = function()
#         vowels = ["a", "o", "e", "i", "u", "y"]
#         result = []
#         for letter in letters:
#             if letter in vowels:
#                 result.append(letter)
#         return result
#
#     return wrapper