inp = [a.strip().split() for a in open("input.txt", "r").readlines()]
inp = [[a[0], int(a[1])] for a in inp]


def move_right(tail_num):
    if tail_num == 0:
        tails[tail_num][0] += 1

    if tails[tail_num][0] < tails[tail_num-1][0]:
        tails[tail_num][0] += 1
        if tails[tail_num][1] < tails[tail_num-1][1]:
            tails[tail_num][1] += 1
        elif tails[tail_num][1] > tails[tail_num-1][1]:
            tails[tail_num][1] -= 1


def move_left(tail_num):
    if tail_num == 0:
        tails[tail_num][0] -= 1
    if tails[tail_num][0] > tails[tail_num-1][0]:
        tails[tail_num][0] -= 1
        if tails[tail_num][1] < tails[tail_num-1][1]:
            tails[tail_num][1] += 1
        elif tails[tail_num][1] > tails[tail_num-1][1]:
            tails[tail_num][1] -= 1


def move_up(tail_num):
    if tail_num == 0:
        tails[tail_num][1] += 1

    elif tails[tail_num][1] < tails[tail_num-1][1]:
        tails[tail_num][1] += 1
        if tails[tail_num][0] < tails[tail_num-1][0]:
            tails[tail_num][0] += 1
        elif tails[tail_num][0] > tails[tail_num-1][0]:
            tails[tail_num][0] -= 1


def move_down(tail_num):
    if tail_num == 0:
        tails[tail_num][1] -= 1

    elif tails[tail_num][1] > tails[tail_num-1][1]:
        tails[tail_num][1] -= 1
        if tails[tail_num][0] < tails[tail_num-1][0]:
            tails[tail_num][0] += 1
        elif tails[tail_num][0] > tails[tail_num-1][0]:
            tails[tail_num][0] -= 1


tail_visited = []
tails = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(tails)):
    tails[i] = [0, 0]

for instruction in inp:
    for i in range(instruction[1]):
        for tail in range(len(tails)):
            if instruction[0] == 'R':
                move_right(tail)
            elif instruction[0] == 'L':
                move_left(tail)
            elif instruction[0] == 'U':
                move_up(tail)
            else:
                move_down(tail)

        tail_visited.append(tails[9])

t_v = []

for v in tail_visited:
    if v not in t_v:
        t_v.append(v)
print(t_v)

# biggest_x = 0
# biggest_y = 0
#
# for i in t_v:
#     if i[0] > biggest_x:
#         biggest_x = i[0]
#
# for i in t_v:
#     if i[1] > biggest_y:
#         biggest_y = i[1]

# print_list = []
#
# for i in range(biggest_y+1):
#     print_list.append([])
#     for k in range(biggest_x+1):
#         print_list[i].append(".")
#
# for x, y in t_v:
#     print_list[y][x] = "#"
#
# print_list.reverse()
# for i in print_list:
#     print(i)

print(len(t_v))
