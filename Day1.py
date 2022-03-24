# part 1
mylist = []

with open("Day1input.txt") as f:
    for line in f:
        mylist.append(int(line))

print(sum(mylist))

# 1 liner
print(sum([int(line) for line in open('Day1input.txt')]))

#part 2
count = 0
total = 0
reached = set()
while True:
    total += mylist[count % len(mylist)]
    if total in reached:
        print(total)
        break
    else:
        reached.add(total)
    count += 1