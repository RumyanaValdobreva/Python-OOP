def reverse_text(string):
    current_letter = len(string) - 1
    end_of_string = 0

    while current_letter >= end_of_string:
        yield string[current_letter]
        current_letter -= 1