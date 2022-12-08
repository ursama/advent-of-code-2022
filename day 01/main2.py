totals = []
elf_food = 0
top_three_sum = 0

with open("input.txt", mode="r") as data:
    data = data.readlines()
    for line in data:
        if line != "\n":
            elf_food += int(line)
        else:
            totals.append(elf_food)
            elf_food = 0

for _ in range(3):
    top_three_sum += max(totals)
    totals.remove(max(totals))

print(top_three_sum)
