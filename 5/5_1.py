from curses.ascii import isalpha


def split_list(l: list, splitter):
    return l[:l.index(splitter)], l[l.index(splitter)+1:]
stacks, instructions = split_list(open("input.txt", "r").readlines(), "\n")
instructions = [inst.strip() for inst in instructions]
stacks = [inst.replace("\n", "") for inst in stacks]

num_of_stacks = len(stacks[-1].replace(" ", ""))

s = [[] for i in range(num_of_stacks)]

for line in stacks[:-1]:
    for i in range(num_of_stacks):
        if line[i*4+1].isalpha():
            s[i].append(line[i*4+1])


print(s)
print(stacks, instructions)

