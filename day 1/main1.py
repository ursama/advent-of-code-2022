totals = []
elf_food = 0

with open("input.txt", mode="r") as data:
    data = data.readlines()
    for line in data:
        if line != "\n":
            elf_food += int(line)
        else:
            totals.append(elf_food)
            elf_food = 0

print(max(totals))
