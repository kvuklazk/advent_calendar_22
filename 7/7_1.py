inp = open("input.txt", "r")

fsys = "/"

for line in inp:
    print(line)
    if line[0] == "$":
        command = line[2:].strip().split(" ")
        print(command)
        if len(command) > 1:
            if command[1] == "/":
                curr_dir = ["/"]
            elif command[1] == "..":
                curr_dir.pop(-1)
            else:
                print("x"*100, "x")
                fsys[1].append([command[1], [], []])
                curr_dir.append(command[1])

# nevim
print(fsys)


