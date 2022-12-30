rows = [item.strip() for item in open("input.txt", "r").readlines()]
columns = []
for i in range(len(rows[0])):
    columns.append("")
    for row in rows:
        columns[i] = columns[i] + row[i]


def find_scenic_score(r, c, t, i_tree, i_row):
    left = [int(x) for x in list(r[:i_tree])[::-1]]
    t = int(t)

    return


trees = []
for i_r, row in enumerate(rows):
    trees.append([])
    for i_t, tree in enumerate(row):
        trees[i_r].append([tree])

        trees[i_r][i_t].append(find_scenic_score(row, columns[i_r], tree, i_t, i_r))


sum_trees = 0
for i in trees:
    for k in i:
        if k[1] == 'seen':
            sum_trees += 1
print(sum_trees)
