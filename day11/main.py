from copy import deepcopy

input = open("./day11/input.txt", "r")
input_rows = []

for line in input:
    input_rows.append(line.strip("\n"))

input.close()

rows = []

for row in input_rows:
    rows.append(list(row))

## PART 1

def num_adjacent_occupied(rows, row_number, column_number):
    row = rows[row_number]
    row_above = rows[row_number - 1] if row_number > 0 else list(range(len(row)))
    row_below = rows[row_number + 1] if row_number < len(rows) - 1 else list(range(len(row)))

    up = row_above[column_number]
    down = row_below[column_number]
    left = row[column_number - 1] if column_number > 0 else None
    right = row[column_number + 1] if column_number < len(row) - 1 else None
    up_left = row_above[column_number - 1] if column_number > 0 else None
    up_right = row_above[column_number + 1] if column_number < len(row_above) - 1 else None
    down_left = row_below[column_number - 1] if column_number > 0 else None
    down_right = row_below[column_number + 1] if column_number < len(row_below) - 1 else None

    count = 0

    if up == "#":
        count += 1
    if down == "#":
        count += 1
    if left == "#":
        count += 1
    if right == "#":
        count += 1
    if up_left == "#":
        count += 1
    if up_right == "#":
        count += 1
    if down_left == "#":
        count += 1
    if down_right == "#":
        count += 1

    return count


def part1():
    past_rows = []
    current_rows = deepcopy(rows)

    while (past_rows != current_rows):
        new_rows = deepcopy(current_rows)

        for row_number in range(len(current_rows)):
            for column_number in range(len(current_rows[row_number])):
                seat = current_rows[row_number][column_number]
                count_adjacent_occupied = num_adjacent_occupied(current_rows, row_number, column_number)

                # seat empty and num adjacent occupied is zero, then becomes occupied
                if seat == "L" and count_adjacent_occupied == 0:
                    new_rows[row_number][column_number] = "#"
                # seat occupied and num adjacent occupied >= 4, then becomes empty
                elif seat == "#" and count_adjacent_occupied >= 4:
                    new_rows[row_number][column_number] = "L"

        past_rows = deepcopy(current_rows)
        current_rows = deepcopy(new_rows)

    count = 0

    for row in current_rows:
        for seat in row:
            if seat == "#":
                count += 1

    return count


print("Number of occupied seats: " + str(part1()))


## PART 2

def num_adjacent_occupied_direction(rows, row_number, column_number):
    up = None
    down = None
    left = None
    right = None
    up_left = None
    up_right = None
    down_left = None
    down_right = None

    # FIND UP
    for test_row in reversed(range(0, row_number)):
        new_seat = rows[test_row][column_number]

        if (up != "#" and new_seat == "#"):
            up = "#"

    # FIND DOWN
    for test_row in range(row_number + 1, len(rows)):
        new_seat = rows[test_row][column_number]

        if (down != "#" and new_seat == "#"):
            down = "#"

    # FIND LEFT
    for test_col in reversed(range(0, column_number)):
        new_seat = rows[row_number][test_col]

        if (left != "#" and new_seat == "#"):
            left = "#"

    # FIND RIGHT
    for test_col in range(column_number + 1, len(rows[row_number])):
        new_seat = rows[row_number][test_col]

        if (right != "#" and new_seat == "#"):
            right = "#"

    # FIND UP LEFT
    test_row = row_number - 1
    test_col = column_number - 1

    while (test_row >= 0 and test_col >= 0):
        new_seat = rows[test_row][test_col]

        if (up_left != "#" and new_seat == "#"):
            up_left = "#"

        test_row -= 1
        test_col -= 1

    # FIND UP RIGHT
    test_row = row_number - 1
    test_col = column_number + 1

    while (test_row >= 0 and test_col < len(rows[row_number])):
        new_seat = rows[test_row][test_col]

        if (up_right != "#" and new_seat == "#"):
            up_right = "#"

        test_row -= 1
        test_col += 1

    # FIND DOWN LEFT
    test_row = row_number + 1
    test_col = column_number - 1

    while (test_row < len(rows) and test_col >= 0):
        new_seat = rows[test_row][test_col]

        if (down_left != "#" and new_seat == "#"):
            down_left = "#"

        test_row += 1
        test_col -= 1

    # FIND DOWN RIGHT
    test_row = row_number + 1
    test_col = column_number + 1

    while (test_row < len(rows) and test_col < len(rows[row_number])):
        new_seat = rows[test_row][test_col]

        if (down_right != "#" and new_seat == "#"):
            down_right = "#"

        test_row += 1
        test_col += 1


    count = 0

    if up == "#":
        count += 1
    if down == "#":
        count += 1
    if left == "#":
        count += 1
    if right == "#":
        count += 1
    if up_left == "#":
        count += 1
    if up_right == "#":
        count += 1
    if down_left == "#":
        count += 1
    if down_right == "#":
        count += 1
    
    return count


def part2():
    past_rows = []
    current_rows = deepcopy(rows)

    while (past_rows != current_rows):
        new_rows = deepcopy(current_rows)

        for row_number in range(len(current_rows)):
            for column_number in range(len(current_rows[row_number])):
                seat = current_rows[row_number][column_number]
                count_adjacent_occupied = num_adjacent_occupied_direction(current_rows, row_number, column_number)

                # seat empty and num adjacent occupied is zero, then becomes occupied
                if seat == "L" and count_adjacent_occupied == 0:
                    new_rows[row_number][column_number] = "#"
                # seat occupied and num adjacent occupied >= 5, then becomes empty
                elif seat == "#" and count_adjacent_occupied >= 5:
                    new_rows[row_number][column_number] = "L"

        past_rows = deepcopy(current_rows)
        current_rows = deepcopy(new_rows)

    count = 0

    for row in current_rows:
        for seat in row:
            if seat == "#":
                count += 1

    return count


print("Number of occupied seats: " + str(part2()))

