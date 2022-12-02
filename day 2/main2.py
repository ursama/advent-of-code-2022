opponent = ["A", "B", "C"]
result = ["X", "Y", "Z"]
total_score = 0


def referee(res):
    global total_score
    opp_figure = opponent.index(res[0])
    my_result = res[1]
    if my_result == "Y":
        total_score += opp_figure + 1
    elif my_result == "X":
        if opp_figure > 0:
            total_score += opp_figure
        else:
            total_score += 3
    else:
        if opp_figure < 2:
            total_score += opp_figure + 2
        else:
            total_score += 1


with open("input.txt", mode="r") as file:
    data = file.readlines()
    data = [x.split() for x in data]

for r in data:
    total_score += result.index(r[1]) * 3
    referee(r)

print(total_score)
