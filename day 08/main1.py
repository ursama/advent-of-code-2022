visible = 0

with open("input.txt", mode="r") as file:
    grid = [x.replace("\n", "") for x in file.readlines()]


def checking_hor(string, check, first, last):
    for x in range(first, last):
        if check <= string[x]:
            return False
    return True


def checking_ver(check, ind, first, last):
    for x in range(first, last):
        if check <= grid[x][ind]:
            return False
    return True


columns = len(grid[0])
for row in grid:
    if grid.index(row) in (0, len(grid) - 1):
        visible += len(row)
    else:
        visible += 2
        for nr in range(1, columns - 1):
            left = checking_hor(row, row[nr], 0, nr)
            right = checking_hor(row, row[nr], nr + 1, columns)
            top = checking_ver(row[nr], nr, 0, grid.index(row))
            bottom = checking_ver(row[nr], nr, grid.index(row) + 1, len(grid))

            if left or right or top or bottom:
                visible += 1

print(visible)
