char_processed = 3
marker_found = False

with open("input.txt", mode="r") as file:
    data = ''.join(file.readlines())

while not marker_found:
    char_processed += 1
    last_four = data[char_processed - 4:char_processed]
    temporary = last_four
    for char in last_four:
        if char in temporary:
            temporary = temporary.replace(char, "")
            marker_found = True
        else:
            marker_found = False
            break


print(char_processed)
