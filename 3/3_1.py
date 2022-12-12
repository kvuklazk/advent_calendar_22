input = open("input.txt", "r")

rucksacks = []
for rucksack in input:
    rucksack = rucksack.strip()
    rucksacks.append([rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]])

items = []
for rucksack in rucksacks:
    i = 0
    while rucksack[0][i] not in rucksack[1]:
        i += 1
    items.append(rucksack[0][i])

sum = 0

for item in items:
    if item.islower():
        sum += ord(item)-96
    else:
        sum += ord(item)-64+26

print(sum)