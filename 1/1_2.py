input = open('input.txt', "r")

elves = [[]]

elf_num = 0
for line in input:
    if line != "\n":
        elves[elf_num].append(line.strip())
    else:
        elf_num += 1
        elves.append([])

elves_sum = []
for elf, snacks in enumerate(elves):
    elves_sum.append(0)
    for snack in snacks:
        elves_sum[elf] += int(snack)

sum_top_3 = 0
for i in range(3):
    sum_top_3 += max(elves_sum)
    elves_sum.remove(max(elves_sum))

print(sum_top_3)
