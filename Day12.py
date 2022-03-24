from collections import defaultdict

file = open('day12input.txt', 'r').read().split('\n')

plant = '#'
none = '.'

shift = 5
buffer = 5

initial = [none for i in range(buffer)] + list(file[0]) + [none for i in range(buffer)]
print(''.join(initial))

file = [i.split() for i in file[2:]]
state_changes = defaultdict(lambda: none)
for change in file:
    state_changes[change[0]] = change[2]

generations = {}


for gen in range(500):
    count = 0
    new = [i for i in initial]
    for plant in range(2, len(initial)-2):
        new[plant] = state_changes[''.join(initial[plant-2:plant + 3])]
        if new[plant] != none:
            count += (plant - shift)
    initial = [i for i in new]

    if plant in initial[:buffer]:
        initial = [none for i in range(buffer)] + initial
        shift += buffer

    if not all(i == none for i in initial[-buffer:]):
        initial = initial + [none for i in range(buffer)]

    if 495 <= (gen + 1) <= 500:
        generations[gen + 1] = count

# Part 1
#print(generations[20])

# Part 2
print(generations)

# TESTING
# for key in generations.keys():
#     try:
#         print(generations[key] - generations[key - 1])
#     except:
#         pass

# Difference of 73 between each generation so 500 * 73 + c = 36877 => c = 377

print(50000000000 * 73 + 377)
