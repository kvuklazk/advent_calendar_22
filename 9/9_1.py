inp = [a.strip().split() for a in open("input.txt", "r").readlines()]
inp = [[a[0], int(a[1])] for a in inp]

h = [0, 0]  # (column, row)
t = [0, 0]


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


tail_visited = [[0, 0]]

for instruction in inp:
    print(instruction, h, t)
    print("begoin", tail_visited)
    for i in range(instruction[1]):
        if instruction[0] == 'R':
            move_right()
        elif instruction[0] == 'L':
            move_left()
        elif instruction[0] == 'U':
            move_up()
        else:
            move_down()
    print(t)
    print("b", tail_visited)
    tail_visited.append(t)
    print("a", tail_visited)

print(h, t)
print(tail_visited)
