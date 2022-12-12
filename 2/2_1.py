input = open("input.txt", "r")

points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
lost = ["AZ", "BX", "CY"]
win = ["AY", "BZ", "CX"]
draw = ["AX", "BY", "CZ"]

total_sum = 0
for line in input:
    if line.replace("\n", "").replace(" ", "") in draw:
        total_sum += 3
    if line.replace("\n", "").replace(" ", "") in win:
        total_sum += 6
    total_sum += points[line.replace("\n", "").replace(" ", "")[1]]
print(total_sum)

