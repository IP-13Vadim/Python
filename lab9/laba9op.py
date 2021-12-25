def count_letters_frequency(input_string):

    literals = {}

    for char in input_string.lower():
        if char in literals:
            literals[char] += 1
        else:
            literals[char] = 1

    return literals


def max_frequency(letters):
    max_frequent_letter = max(letters, key=letters.get)
    return f'"{max_frequent_letter}" had {letters.get(max_frequent_letter)}'


def min_frequency(letters):
    min_frequent_letter = min(letters, key=letters.get)
    return f'"{min_frequent_letter}" had {letters.get(min_frequent_letter)}'


input = "how to learn english effectively"
literals = count_letters_frequency(input)
print(literals)
print(max_frequency(literals))
print(min_frequency(literals))