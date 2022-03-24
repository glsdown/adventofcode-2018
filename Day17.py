
spring = [500, 0] # x, y - column, row

data = open('day17testinput.txt').read().splitlines()

pairs = []
max_values = {'x': 0, 'y': 0}
min_values = {'x' : 500, 'y': 500}

for line in data:

    first, second = line.split(', ')

    first_letter = first[0]
    first_letter_value = int(first[2:])
    second_letter = second[0]

    max_values[first_letter] = max(first_letter_value, max_values[first_letter])
    min_values[first_letter] = min(first_letter_value, min_values[first_letter])

    min_second_letter = int(second[2:].split('..')[0])
    max_second_letter = int(second[2:].split('..')[1])

    max_values[second_letter] = max(max_second_letter, max_values[second_letter])
    min_values[second_letter] = min(min_second_letter, min_values[second_letter])

    for i in range(min_second_letter, max_second_letter+1):

        pairs.append({first_letter : first_letter_value, second_letter: i})

print(min_values, max_values)

grid = [['.' for x in range(min_values['x']-1, max_values['x']+2)] for y in range(min_values['y'], max_values['y']+1)]

x_offset = min_values['x'] - 1
y_offset = min_values['y']

for pair in pairs:
    grid[pair['y'] - y_offset][pair['x'] - x_offset] = 'C'

for line in grid:
    print(''.join(line))


def water_flow(x, y):

    column = [row[x - x_offset] for row in grid]
    count = 0

    if all(i == '.' for i in column[y+1:]):
        return len(column)

    else:
        for row in column:
            # if its sand continue down
            if row == '.':
                count += 1
                grid[y - y_offset][x - x_offset] = '|'
                y += 1
            # if its already water trickling down, don't count it and stop (covered elsewhere)
            elif row == '|':
                return count
            # if it reaches clay or still water, then need to check if it needs to continue or not
            elif row == "C" or row == "W":
                clay_left = True
                clay_right = True

                while clay_left and clay_right:

                    left = 0
                    right = 0
                    while True:
                        if x - x_offset - left < 0:
                            # Reached the edge of the water - need to 'overflow'
                            clay_left = False
                            break
                        elif grid[y - y_offset][x - x_offset - left] == 'C':
                            break
                        else:
                            left += 1

                    while True:
                        if x - x_offset + right > max_values['x']+1:
                            # Reached the edge of the water - need to 'overflow'
                            clay_right = False
                            break
                        elif grid[y - y_offset][x - x_offset + right] == 'C':
                            break
                        else:
                            right += 1

                    if clay_left and clay_right:
                        for change in range(-left + 1, right):
                            if grid[y - y_offset][x - x_offset + change] == '.':
                                count += 1
                            grid[y - y_offset][x - x_offset + change] = 'W'

                    elif clay_left:
                        count += water_flow(x + right + 2, y)
                    elif clay_right:
                        count += water_flow(x - left - 2, y)
                    else:
                        count += water_flow(x - left - 2, y)
                        count += water_flow(x + right + 2, y)
                    y = y - 1

        return count


water_flow(500, 0)

for line in grid:
    print(''.join(line))


