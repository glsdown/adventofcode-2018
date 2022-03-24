from collections import Counter
twos = 0
threes = 0

with open('Day2input.txt') as f:
    for line in f:
        two_present = False
        three_present = False
        counter = Counter(line.strip())
        for letter in line.strip():
            if counter[letter] == 2:
                two_present = True
            elif counter[letter] == 3:
                three_present = True
            if two_present and three_present:
                break
        if two_present:
            twos += 1
        if three_present:
            threes += 1
print(twos * threes)
