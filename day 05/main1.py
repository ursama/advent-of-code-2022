stacks = []
instructions = []
nr = 1
top_crates = ''

with open("input.txt", mode='r') as file:
    data = [x.strip("\n") for x in file.readlines()]

stacking = True
for line in data:
    if line == '':
        stacking = False
        continue

    if stacking:
        stacks.append(line)
    else:
        instructions.append(line)

stacks = [stack.translate({ord(i): None for i in '[] '}) for stack in stacks]
instructions = [" ".join(instruction.translate({ord(i): None for i in 'movefrt'}).split()).split(' ') for instruction in instructions]

for instruction in instructions:
    for _ in range(0, int(instruction[0])):
        crate = stacks[int(instruction[1]) - 1][-1]
        stacks[int(instruction[1]) - 1] = stacks[int(instruction[1]) - 1][:-1]
        stacks[int(instruction[2]) - 1] += crate

for stack in stacks:
    top_crates += stack[-1]

print(top_crates)
