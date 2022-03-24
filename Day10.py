import matplotlib.pyplot as plt

lines = [line.strip().split('> ') for line in open('Day10input.txt', 'r')]
lines = [[line[0].split("=<")[1], line[1].split("=<")[1][:-1]] for line in lines]
lines = [[int(i) for i in line[0].split(', ')] + [int(i) for i in line[1].split(', ')] for line in lines]

lines = [{'x': line[0], 'y': line[1], 'xchange': line[2], 'ychange': line[3]} for line in lines]

seconds = 0

min_x = 0
max_x = 0
min_y = 0
max_y = 0

for line in lines:
    max_x = max(max_x, line['x'])
    min_x = min(min_x, line['x'])
    max_y = max(max_y, line['y'])
    min_y = min(min_y, line['y'])

min_spread = (max_x - min_x) * (max_y - min_y)


while True:
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    for line in lines:
        line['x'] += line['xchange']
        line['y'] += line['ychange']
        max_x = max(max_x, line['x'])
        min_x = min(min_x, line['x'])
        max_y = max(max_y, line['y'])
        min_y = min(min_y, line['y'])

    spread = (max_x - min_x) * (max_y - min_y)

    if spread > min_spread:
        print(seconds)
        break
    else:
        min_spread = spread

    seconds += 1


for line in lines:
    line['x'] -= line['xchange']
    line['y'] -= line['ychange']

x = [line['x'] for line in lines]
y = [-line['y'] for line in lines]

plt.plot(x, y, 'o', color='black')
plt.legend()
plt.show()



