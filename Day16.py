from collections import defaultdict

#Addition:
def addr(registers, a, b):
    return registers[a] + registers[b]
def addi(registers, a, b):
    return registers[a] + b

#Multiplication:
def mulr(registers, a, b):
    return registers[a] * registers[b]
def muli(registers, a, b):
    return registers[a] * b

#Bitwise AND:

def banr(registers, a, b):
    return registers[a] & registers[b]
def bani(registers, a, b):
    return registers[a] & b

#Bitwise OR:
def borr(registers, a, b):
    return registers[a] | registers[b]
def bori(registers, a, b):
    return registers[a] | b

#Assignment:
def setr(registers, a, b):
    return registers[a]
def seti(registers, a, b):
    return a

#Greater-than testing:
def gtir(registers, a, b):
    return int(a > registers[b])
def gtri(registers, a, b):
    return int(registers[a] > b)
def gtrr(registers, a, b):
    return int(registers[a] > registers[b])

#Equality testing:
def eqir(registers, a, b):
    return int(a == registers[b])
def eqri(registers, a, b):
    return int(registers[a] == b)
def eqrr(registers, a, b):
    return int(registers[a] == registers[b])

test_program = open('day16input.txt').read().splitlines()

opcodes = [
    addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr
]
opcode_matches = defaultdict(list)

total = 0
for line in range(0,len(test_program),4):

    original = [int(i) for i in test_program[line].split(':')[1].strip()[1:-1].split(', ')]

    command = [int(i) for i in test_program[line + 1].split()]

    new = [int(i) for i in test_program[line + 2].split(':')[1].strip()[1:-1].split(', ')]

    count = 0
    possible = set()
    for opcode in opcodes:
        a,b,c = command[1:]
        check = [i for i in original]
        check[c] = opcode(original, a, b)

        if check == new:
            count += 1
            possible.add(opcode)

    # Part 1
    if count >= 3:
        total += 1

    # Part 2
    opcode_matches[command[0]].append(possible)

# part 1
print(total)

# part 2
selected = dict()

for opcode in opcode_matches.keys():

    choices = opcode_matches[opcode]
    selected[opcode] = set(opcodes).intersection(*choices)

complete = 0

final = dict()
while complete < 16:

    for opcode in selected.keys():
        if len(selected[opcode]) == 1:
            complete += 1
            final[opcode] = next(iter(selected[opcode]))
            selected[opcode] = set()
            for other_codes in selected.keys():
                if final[opcode] in selected[other_codes]:
                    selected[other_codes].remove(final[opcode])

print(final)

commands = [[int(j) for j in i.split()] for i in open('day16codeinput.txt').read().splitlines()]
registers = [0, 0, 0, 0]

for opcode, a, b, c  in commands:
    registers[c] = final[opcode](registers, a, b)

print(registers)




