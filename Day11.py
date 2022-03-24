serial = 1955

grid = [[0 for i in range(300)] for j in range(300)]

for x in range(300):
    for y in range(300):
        rack_id = (x+1) + 10
        power = rack_id * (y+1)
        power = power + serial
        power *= rack_id
        if len(str(abs(power))) < 3:
            power = 0
        else:
            power = int(str(abs(power))[-3])
        power -= 5
        grid[x][y] = power

max_power = 0
max_coords = [0,0]

for x in range(300):
    for y in range(300):
        for size in range(1, min(300 - x, 300 - y)):
            power = sum([sum(item[y: y + size]) for item in grid[x: x + size]])
            # power = 0
            # for x_shift in range(size):
            #     for y_shift in range(size):
            #         power += grid[x + x_shift][y + y_shift]
            if power > max_power:
                max_power = power
                max_coords = [x + 1, y + 1, size]
    print(x)

print(max_coords, max_power)
