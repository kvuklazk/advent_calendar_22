inp = [a.strip().split() for a in open("input.txt", "r").readlines()]
inp = [[a[0], int(a[1])] for a in inp]


def move_right():

    if t[0] < h[0]:
        t[0] += 1
        if t[1] < h[1]:
            t[1] += 1
        elif t[1] > h[1]:
            t[1] -= 1
    h[0] += 1


def move_left():
    if t[0] > h[0]:
        t[0] -= 1
        if t[1] < h[1]:
            t[1] += 1
        elif t[1] > h[1]:
            t[1] -= 1
    h[0] -= 1


def move_up():
    if t[1] < h[1]:
        t[1] += 1
        if t[0] < h[0]:
            t[0] += 1
        elif t[0] > h[0]:
            t[0] -= 1
    h[1] += 1


def move_down():

    if t[1] > h[1]:
        t[1] -= 1
        if t[0] < h[0]:
            t[0] += 1
        elif t[0] > h[0]:
            t[0] -= 1

    h[1] -= 1


tail_visited = []
h, t = [0, 0], [0, 0]

for instruction in inp:
    for i in range(instruction[1]):
        if instruction[0] == 'R':
            move_right()
        elif instruction[0] == 'L':
            move_left()
        elif instruction[0] == 'U':
            move_up()
        else:
            move_down()

        tail_visited.append([a for a in t])

t_v = []

for v in tail_visited:
    if v not in t_v:
        t_v.append(v)
print(h, t)
print(t_v)
#
# biggest_x = 0
# biggest_y = 0

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
