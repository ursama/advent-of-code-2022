opponent = ["A", "B", "C"]
me = ["X", "Y", "Z"]
total_score = 0


def referee(res):
    global total_score
    opp_figure = opponent.index(res[0])
    my_figure = me.index(res[1])
    if opp_figure == my_figure:
        total_score += 3
    elif opp_figure != 2:
        if my_figure == opp_figure + 1:
            total_score += 6
    else:
        if my_figure == 0:
            total_score += 6


with open("input.txt", mode="r") as file:
    data = file.readlines()
    data = [x.split() for x in data]

for r in data:
    total_score += me.index(r[1]) + 1
    referee(r)

print(total_score)
