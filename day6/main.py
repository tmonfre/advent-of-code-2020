input = open("./day6/input.txt", "r")
rows = []

for line in input:
    rows.append(line)

input.close()

original_rows = rows

## PART 1

for i in range(len(rows)):
    rows[i] = rows[i].strip("\n")

groups = [""]
index = 0

for row in rows:
    if len(row) > 0:
        groups[index] += row
    else:
        index += 1
        groups.append("")

sum = 0

for group in groups:
    group_set = set()

    for form in group:
        group_set.add(form)

    sum += len(group_set)

print("Sum of group count: " + str(sum))

## PART 2

rows = original_rows

for i in range(len(rows)):
    rows[i] = rows[i].strip("\n")

groups = [""]
index = 0

for row in rows:
    if len(row) > 0:
        groups[index] += row if len(groups[index]) == 0 else " " + row
    else:
        index += 1
        groups.append("")

output_groups = []

for group in groups:
    output_groups.append(group.split(' '))

groups = output_groups

sum = 0

for group in groups:
    group_count = {}

    for member in group:
        member_set = set()

        for form in member:
            if form not in group_count:
                group_count[form] = 0

            if form not in member_set:
                group_count[form] += 1
                member_set.add(form)

    match_count = 0

    for form in group_count:
        if group_count[form] == len(group):
            match_count += 1

    sum += match_count

print("Sum of group match count: " + str(sum))
