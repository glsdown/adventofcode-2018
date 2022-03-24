from collections import defaultdict

steps = [line.strip().split() for line in open('day7input.txt', 'r')]

steps = [[x[1], x[7]] for x in steps]

prerequisites = defaultdict(list)
letters = set()

for first, second in steps:
    prerequisites[second].append(first)
    letters.add(first)
    letters.add(second)

letters = list(letters)
letters.sort()
all_letters = [i for i in letters]

first_step = [letter for letter in letters if len(prerequisites[letter]) == 0][0]
sequence = first_step
letters.pop(letters.index(first_step))

while len(letters) > 0:
    for i in range(len(letters)):
        if all([j in sequence for j in prerequisites[letters[i]]]):
            sequence += letters[i]
            letters.pop(i)
            break

print(sequence)

# PART 2 ###############
alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()

time_taken = {i: 61 + alpha.index(i) for i in all_letters}

elves = {i: {"time_left": 0, "task": ""} for i in range(5)}

letters = [i for i in all_letters]
sequence = ""
started = []

minute = 0

while len(letters) > 0:

    minute += 1

    for i in range(len(letters)):
        if all([j in sequence for j in prerequisites[letters[i]]]) and (letters[i] not in started):
            available_elves = [i for i in elves.keys() if elves[i]["time_left"] == 0]
            if len(available_elves) > 0:
                elves[available_elves[0]]["time_left"] = time_taken[letters[i]]
                elves[available_elves[0]]["task"] = letters[i]
                started.append(letters[i])

    for elf in elves.keys():
        if elves[elf]["task"] != "":
            elves[elf]["time_left"] -= 1
        if elves[elf]["time_left"] == 0 and elves[elf]["task"] != "":
            sequence += elves[elf]["task"]
            letters.pop(letters.index(elves[elf]["task"]))
            elves[elf]["task"] = ""

print(minute)