scores = []

with open("input.txt", mode="r") as file:
    grid = [x.replace("\n", "") for x in file.readlines()]


def checking_hor(string: str, check: str, first: int, last: int, change:int):
    trees_visible = 0
    for x in range(first, last, change):
        if check <= string[x]:
            return trees_visible + 1
        trees_visible += 1
    return trees_visible


def checking_ver(check: str, ind: int, first: int, last: int, change: int):
    trees_visible = 0
    for x in range(first, last, change):
        if check <= grid[x][ind]:
            return trees_visible + 1
        trees_visible += 1
    return trees_visible


columns = len(grid[0])
for row in grid:
    if grid.index(row) not in (0, len(grid) - 1):
        for nr in range(1, columns - 1):
            left = checking_hor(row, row[nr], nr - 1, -1, -1)
            right = checking_hor(row, row[nr], nr + 1, columns, 1)
            top = checking_ver(row[nr], nr, grid.index(row) - 1, -1, -1)
            bottom = checking_ver(row[nr], nr, grid.index(row) + 1, len(grid), 1)
            print(left, right, top, bottom)
            scores.append(left * right * top * bottom)

print(max(scores))
