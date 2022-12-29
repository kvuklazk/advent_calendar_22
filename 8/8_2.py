from functools import reduce  # Required in Python 3
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

rows = [a.strip() for a in open("input.txt", "r").readlines()]
rows = [list(a) for a in rows]
for r, row in enumerate(rows):
    for i in range(len(row)):
        rows[r][i] = int(rows[r][i])

collumns = []
for i in range(len(rows[0])):
    collumns.append([])

for row in rows:
    for i in range(len(row)):
        collumns[i].append(int(row[i]))


def scenic_score(row, collumn, tree, i_r, i_t):
    scores = []

    scores.append(row[:i_t][::-1])

    scores.append(row[i_t + 1:])

    scores.append(collumn[:i_r][::-1])

    scores.append(collumn[i_r + 1:])

    return prod([trees_seen(a, tree) for a in scores])


def trees_seen(trees, tree):
    count = 0
    if trees:
        while count < len(trees):
            if trees[count] >= tree:
                count += 1
                break
            count += 1
    return count


trees = []

for i_r, row in enumerate(rows):
    trees.append([])
    for i_t, tree in enumerate(row):
        trees[i_r].append(scenic_score(row, collumns[i_t], tree, i_r, i_t))


highest = 0
for i in trees:
    for k in i:
        if k > highest:
            highest = k
print(highest)
