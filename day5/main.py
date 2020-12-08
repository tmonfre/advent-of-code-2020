input = open("./day5/input.txt", "r")
rows = []

for line in input:
    rows.append(line)

input.close()

## PART 1

max_seat_id = 0

for row in rows:
    columns = list(range(128))
    index = 0

    while len(columns) > 1:
        midpoint_index = int(len(columns) / 2) - 1

        if row[index] == 'F':
            columns = columns[0:midpoint_index+1]
        elif row[index] == 'B':
            columns = columns[midpoint_index+1:]

        index += 1

    row_number = columns[0]

    seats = list(range(8))

    while len(seats) > 1:
        midpoint_index = int(len(seats) / 2) - 1

        if row[index] == 'L':
            seats = seats[0:midpoint_index+1]
        elif row[index] == 'R':
            seats = seats[midpoint_index+1:]

        index += 1

    seat_number = seats[0]

    seat_id = (row_number * 8) + seat_number

    if (seat_id > max_seat_id):
        max_seat_id = seat_id

print("Highest seat ID: " + str(max_seat_id))


## PART 2

seat_ids = []

for row in rows:
    columns = list(range(128))
    index = 0

    while len(columns) > 1:
        midpoint_index = int(len(columns) / 2) - 1

        if row[index] == 'F':
            columns = columns[0:midpoint_index+1]
        elif row[index] == 'B':
            columns = columns[midpoint_index+1:]

        index += 1

    row_number = columns[0]

    seats = list(range(8))

    while len(seats) > 1:
        midpoint_index = int(len(seats) / 2) - 1

        if row[index] == 'L':
            seats = seats[0:midpoint_index+1]
        elif row[index] == 'R':
            seats = seats[midpoint_index+1:]

        index += 1

    seat_number = seats[0]

    seat_ids.append((row_number * 8) + seat_number)

seat_ids.sort()

my_seat = None

for i in range(len(seat_ids) - 1):
    if seat_ids[i + 1] != seat_ids[i] + 1:
        my_seat = seat_ids[i] + 1

print("My seat is: " + str(my_seat))
