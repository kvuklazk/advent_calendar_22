assignments = open("input.txt", "r").readlines()
assignments = [item.strip().split(",") for item in assignments]
assignments = [[i[0].split("-"), i[1].split("-")] for i in assignments]
ass = []
for i in assignments:
    ass.append([])
    for a in i:
        ass[-1].append(list(range(int(a[0]), int(a[1])+1)))

sum = 0
for i in ass:
    if any(item in i[1] for item in i[0]):
        sum += 1
print(sum)

