puzzle = '637061'

# debug
#puzzle = '306281'
#check = '20298300'

scoreboard = '37'

current = [0, 1]

while True:
    recipe = sum([int(scoreboard[i]) for i in current])
    scoreboard += str(recipe)
    current = [(i + int(scoreboard[i]) + 1) % len(scoreboard) for i in current]
    if puzzle in scoreboard[-len(puzzle)-2:]:
        print(scoreboard.index(puzzle))
        break



# Part 1
def part_1():
    puzzle = 637061
    scoreboard = [3, 7]

    current = [0, 1]
    count = 2
    while count < puzzle + 10:
        recipe = sum([scoreboard[i] for i in current])
        count += len(str(recipe))
        scoreboard += [int(i) for i in list(str(recipe))]
        current = [(i + scoreboard[i] + 1) % len(scoreboard) for i in current]

    print(''.join([str(i) for i in scoreboard[puzzle: puzzle + 10]]))