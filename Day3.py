claims = []

with open('Day3input.txt') as f:
    for line in f:
        claims.append(line.strip())

fabric = [['O' for i in range(1000)] for j in range(1000)]
count = 0
claims_check = []

for claim in claims:
    items = claim.split('@')
    claim_id = int(items[0].strip()[1:])
    items = items[1].strip().split(':')
    coords = items[0].strip().split(',')
    size = items[1].strip().split('x')
    coords = [int(i) for i in coords]
    size = [int(i) for i in size]

    squares = 0

    for w in range(size[0]):
        for l in range(size[1]):
            new_coord = [coords[0] + w, coords[1] + l]
            if fabric[new_coord[0]][new_coord[1]] == 'X':
                count += 1
                fabric[new_coord[0]][new_coord[1]] = 'P'
            elif fabric[new_coord[0]][new_coord[1]] == 'O':
                fabric[new_coord[0]][new_coord[1]] = 'X'
                squares += 1

    if squares == size[0] * size[1]:
        claims_check.append([claim_id, [i for i in coords], [i for i in size]])

for claim in claims_check:
    coords = [i for i in claim[1]]
    size = [i for i in claim[2]]
    squares = 0

    for w in range(size[0]):
        for l in range(size[1]):
            new_coord = [coords[0] + w, coords[1] + l]
            if fabric[new_coord[0]][new_coord[1]] == 'X':
                squares += 1

    if squares == size[0] * size[1]:
        print(claim[0])

print(count)