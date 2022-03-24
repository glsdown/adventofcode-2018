

with open('Day5input.txt') as f:
    original_polymer = list(f.read().strip())

min_length = len(original_polymer)


for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(letter)

    polymer = [i for i in original_polymer if i not in [letter, letter.upper()]]
    if len(polymer) == len(original_polymer):
        continue

    character = 0
    while character < len(polymer) - 1:
        if abs(ord(polymer[character]) - ord(polymer[character + 1])) == 97 - 65:
            polymer = polymer[:character] + polymer[character + 2:]
            character =max(0, character - 1)
        else:
            character += 1

    if min_length > len(polymer):
        min_length = len(polymer)

print(min_length)

