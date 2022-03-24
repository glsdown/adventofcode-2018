
def differ_by_one(string1, string2):
    if len(string1) == len(string2):
        count_diffs = 0
        for a, b in zip(string1, string2):
            if a != b:
                if count_diffs > 0:
                    return False
                count_diffs += 1
        return True

boxes = []

with open('Day2input.txt') as f:
    for line in f:
        boxes.append(line.strip())

for item in boxes:
    for seconditem in boxes:
        if item == seconditem:
            continue
        else:
            if differ_by_one(item, seconditem):
                print(item, seconditem)
                exit()