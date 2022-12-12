input = open("input.txt", "r")

outcome = {
    "X": ["AC", "BA", "CB"],
    "Y": ["AA", "BB", "CC"],
    "Z": ["AB", "BC", "CA"]
}
points = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 0,
    "Y": 3,
    "Z": 6
}

total_sum = 0
for line in input:
    match = line.strip().split(" ")
    total_sum += points[match[1]]
    result = [i for i in outcome[match[1]] if match[0] in i.split()[0][0]]
    total_sum += points[result[0][1]]
print(total_sum)

