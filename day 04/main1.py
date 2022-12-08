containing = 0

with open("input.txt", mode="r") as file:
    pairs = file.readlines()
    pairs = [x.strip("\n").rsplit(",") for x in pairs]
    pairs = [[x[0].rsplit("-"), x[1].rsplit("-")] for x in pairs]

for pair in pairs:
    contains = False
    first = [x for x in range(int(pair[0][0]), int(pair[0][1]) + 1)]
    second = [x for x in range(int(pair[1][0]), int(pair[1][1]) + 1)]
    for section_id in first:
        if section_id in second:
            contains = True
        else:
            if contains:
                contains = False
            break

    if contains:
        containing += 1
        continue

    for section_id in second:
        if section_id in first:
            contains = True
        else:
            if contains:
                contains = False
            break

    if contains:
        containing += 1

print(containing)
