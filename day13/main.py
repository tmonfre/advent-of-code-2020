import math

input = open("./day13/input.txt", "r")
rows = []

for line in input:
    rows.append(line.strip("\n"))

input.close()

starting_timestamp = int(rows[0])
buses = [int(item) for item in rows[1].split(",") if item != "x"]

## PART 1

min_start = math.inf
min_start_bus_id = None

for bus in buses:
    first_arrival = bus * (math.floor(starting_timestamp / bus) + 1)

    if first_arrival < min_start:
        min_start = first_arrival
        min_start_bus_id = bus

answer = min_start_bus_id * (min_start - starting_timestamp)

print("Product answer: " + str(answer))

## PART 2

offsets = {}
departures = rows[1].split(',')

for i in range(len(departures)):
    if departures[i] != "x":
        offsets[int(departures[i])] = i

timestamp = 0
found = False

while not found:    
    match = True

    for departure in offsets:
        match = match and float.is_integer((timestamp + offsets[departure]) / departure)

    found = match
    timestamp += 1

answer = timestamp - 1

print("First departure time that lines up: " + str(answer))
