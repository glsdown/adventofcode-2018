from collections import deque

players = 424
last = 7148200

# Testing
#players = 30
#last = 5807

# Part 1 ##########
elves = {player: 0 for player in range(players)}

current_player = 0
marbles = [0]
current_position = 0
high_score = 0

# for current_marble in range(1, last + 1):
#
#     if current_marble % 23 != 0:
#         position = (marbles.index(current_position) + 2) % len(marbles)
#         marbles = marbles[:position] + [current_marble] + marbles[position:]
#         current_position = current_marble
#     else:
#         elves[current_player] += current_marble
#         position = (marbles.index(current_position) - 7) % len(marbles)
#         current_position = marbles[(position + 1) % len(marbles)]
#         elves[current_player] += marbles[position]
#         marbles.pop(position)
#         if elves[current_player] > high_score:
#             high_score = elves[current_player]
#
#     current_player = (current_player + 1) % players
#     if current_marble % 10000 == 0:
#         print(current_marble * 100/last, "% through")


# Part 2 ################

marbles = deque(marbles)

for current_marble in range(1, last + 1):
    if current_marble % 23 != 0:
        marbles.rotate(-1)
        marbles.append(current_marble)
    else:
        elves[current_player] += current_marble
        marbles.rotate(7)
        elves[current_player] += marbles.pop()
        marbles.rotate(-1)
        if elves[current_player] > high_score:
            high_score = elves[current_player]

    current_player = (current_player + 1) % players

print(high_score)