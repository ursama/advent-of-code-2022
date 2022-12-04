priorities_sum = 0
backpacks_list = []


def find_badge(items):
    global priorities_sum
    for letter in items[0]:
        for letter2 in items[1]:
            for letter3 in items[2]:
                if letter == letter2 and letter == letter3:
                    if letter.lower() == letter:
                        priorities_sum += ord(letter) - 96
                    else:
                        priorities_sum += ord(letter) - 38
                    return 1


with open("input.txt", mode='r') as file:
    data = file.readlines()


for backpack in data:
    backpacks_list.append(backpack)
    if len(backpacks_list) == 3:
        find_badge(backpacks_list)
        backpacks_list = []


print(priorities_sum)
