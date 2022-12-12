input = open("input.txt", "r").readlines()

groups = []
for group in range(0, int(len(input)), 3):
    groups.append([])
    for i in range(3):
        groups[-1].append(input[group+i].strip())

items = []
for group in groups:
    i = 0
    while group[0][i] not in group[1] or group[0][i] not in group[2]:
        i += 1
    items.append(group[0][i])

sum = 0

for item in items:
    if item.islower():
        sum += ord(item)-96
    else:
        sum += ord(item)-64+26

print(groups, items, "\n", sum)
