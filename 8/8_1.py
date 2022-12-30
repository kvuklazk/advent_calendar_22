rows = [item.strip() for item in open("input.txt", "r").readlines()]
columns = []
for i in range(len(rows[0])):
    columns.append("")
    for row in rows:
        columns[i] = columns[i] + row[i]


def bigger_trees(r, c, t, i_tree, i_row):
    return [[a for a in r[:i_tree] if int(a) >= int(t)],
            [a for a in r[i_tree+1:] if int(a) >= int(t)],
            [a for a in c[:i_row] if int(a) >= int(t)],
            [a for a in c[i_row+1:] if int(a) >= int(t)]]


trees = []
for i_r, row in enumerate(rows):
    trees.append([])
    for i_t, tree in enumerate(row):
        trees[i_r].append([tree])

        # print(bigger_trees(row, columns[i_t], int(tree), i_t, i_r))
        if any(a == [] for a in bigger_trees(row, columns[i_t], int(tree), i_t, i_r)):
            trees[i_r][i_t].append("seen")
        else:
            trees[i_r][i_t].append("hidden")


print(trees)

sum_trees = 0
for i in trees:
    for k in i:
        if k[1] == 'seen':
            sum_trees += 1
print(sum_trees)
