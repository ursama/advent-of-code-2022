priorities_sum = 0


def find_shared(items):
    global priorities_sum
    for letter in items[0]:
        for letter2 in items[1]:
            if letter == letter2:
                if letter.lower() == letter:
                    priorities_sum += ord(letter) - 96
                else:
                    priorities_sum += ord(letter) - 38
                return 1


with open("input.txt", mode='r') as file:
    data = file.readlines()
    data = [[x[:len(x)//2], x[len(x)//2:].rstrip('\n')] for x in data]


for backpack in data:
    find_shared(backpack)

print(priorities_sum)
