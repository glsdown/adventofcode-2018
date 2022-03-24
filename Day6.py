from collections import defaultdict

def distance(a, b):
    return sum([abs(a[i] - b[i]) for i in range(len(a))])

def get_closest(coord, possible):
    distances = [[distance(coord, p), p] for p in possible]
    distances.sort()
    # Check it doesn't have more than one closest point
    if distances[0][0] < distances[1][0]:
        return distances[0][1]
    else:
        return (0, 0)

def get_total_distance(coord, possible):
    return sum(distance(coord, p) for p in possible)

coordinates = [[int(i) for i in line.strip().split(', ')] for line in open('Day6input.txt', 'r')]

coordinates = [(x,y) for x,y in coordinates]

xmin = min([x for x, y in coordinates])
ymin = min([y for x, y in coordinates])
xmax = max([x for x, y in coordinates])
ymax = max([y for x, y in coordinates])

# PART 1 ##################
# grid = defaultdict(int)
#
# infinite = []
#
# for x in range(xmin, xmax+1):
#     infinite.append(get_closest((x, ymin), coordinates))
#     infinite.append(get_closest((x, ymax), coordinates))
#     for y in range(ymin, ymax+1):
#         infinite.append(get_closest((xmin, y), coordinates))
#         infinite.append(get_closest((xmax, y), coordinates))
#         grid[get_closest((x, y), coordinates)] += 1
#
# sorted_grid = [grid[k] for k in grid.keys() if k not in infinite]
# sorted_grid.sort(reverse=True)
# print(sorted_grid[0])

# PART 2 ##################

max_value = 10000
size = 0
buffer = 0

for x in range(xmin-buffer, xmax+buffer+1):
    for y in range(ymin-buffer, ymax+buffer+1):
        if get_total_distance((x, y), coordinates) < max_value:
            size += 1

print(size)
