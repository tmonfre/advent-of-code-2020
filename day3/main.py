input = open("./day3/input.txt", "r")
rows = []

for line in input:
    rows.append(line)

input.close()

## PART 1

base_index = 0
num_trees = 0
row_length = len(rows[0]) - 1

for row in rows:
    value = row[base_index % row_length]
    num_trees += value == '#'
    base_index += 3

print("Number of trees: " + str(num_trees))

## PART 2

base_index = 0
num_trees = 0
row_length = len(rows[0]) - 1

traverse_right_amount = [1, 3, 5, 7, 1]
only_evens = [False, False, False, False, True]
answer = 1
trees = []

for i in range(len(traverse_right_amount)):
    base_index = 0
    num_trees = 0

    for j in range(len(rows)):
        # skip if odd row (proxy for traversing down two)
        if only_evens[i] and j % 2 != 0:
            continue

        row = rows[j]
        value = row[base_index % row_length]
        num_trees += value == '#'
        base_index += traverse_right_amount[i]

    trees.append(num_trees)
    answer *= num_trees

print("Number of trees: " + str(answer))