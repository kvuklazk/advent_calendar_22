# JCMHLVGMG
# LVMRWSSPZ
from enum import Enum


def split_list(spl_l: list, splitter):
    return spl_l[:spl_l.index(splitter)], spl_l[spl_l.index(splitter)+1:]


stacks, instructions = split_list(open("input.txt", "r").readlines(), "\n")
instructions = [inst.strip() for inst in instructions]
stacks = [stack.replace("\n", "") for stack in stacks]

num_of_stacks = len(stacks[-1].replace(" ", ""))

s = [[] for i in range(num_of_stacks)]


for line in stacks[:-1]:
    for i in range(num_of_stacks):
        if i*4+1 < len(line):
            if line[i*4+1].isalpha():
                s[i].append(line[i*4+1])


for instruction in instructions:
    num_to_move, from_stack, to_stack = [int(i) for i in instruction.split() if i.isnumeric()]
    from_stack -= 1
    to_stack -= 1
    for i in s[from_stack][0:num_to_move][::-1]:
        s[to_stack].insert(0, i)
    del s[from_stack][0:num_to_move]

for i in s:
    print(i)
print("".join([i[0] for i in s if i != []]))
