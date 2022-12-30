inp = [a.strip().split() for a in open("input.txt", "r").readlines()]
inp = [[a[0], int(a[1])] for a in inp]

s = []

for i in range(10):
    s.append([])
    for k in range(10):
        s[i].append(".")
s[0][0] = "H"
print(s)

def move_right():
    pass
def move_left():
    pass
def move_up():
    pass
def move_down():
    pass

for instruction in inp:
    print(instruction)
    for i in range(instruction[1]):
        if instruction[0] == 'R':
            move_right()
        elif instruction[0] == 'L':
            move_left()
        elif instruction[0] == 'U':
            move_up()
        else:
            move_down()
