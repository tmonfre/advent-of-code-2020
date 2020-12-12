input = open("./day12/input.txt", "r")
rows = []

for line in input:
    rows.append(line.strip("\n"))

input.close()

## PART 1

def part_1(instructions):
    ship_direction = "E"
    vertical_value = 0
    horizontal_value = 0

    for instruction in instructions:
        command = instruction[0]
        amount = int(instruction[1:])

        # handle movements
        if command == "N" or (command == "F" and ship_direction == "N"):
            vertical_value += amount
        elif command == "S" or (command == "F" and ship_direction == "S"):
            vertical_value -= amount
        elif command == "E" or (command == "F" and ship_direction == "E"):
            horizontal_value += amount
        elif command == "W" or (command == "F" and ship_direction == "W"):
            horizontal_value -= amount

        # handle rotations
        elif command == "L":
            num_changes = int((amount / 360) * 4)

            for i in range(num_changes):
                if ship_direction == "N":
                    ship_direction = "W"
                elif ship_direction == "W":
                    ship_direction = "S"
                elif ship_direction == "S":
                    ship_direction = "E"
                elif ship_direction == "E":
                    ship_direction = "N"

        elif command == "R":
            num_changes = int((amount / 360) * 4)

            for i in range(num_changes):
                if ship_direction == "N":
                    ship_direction = "E"
                elif ship_direction == "E":
                    ship_direction = "S"
                elif ship_direction == "S":
                    ship_direction = "W"
                elif ship_direction == "W":
                    ship_direction = "N"


    return abs(vertical_value) + abs(horizontal_value)

print(part_1(rows))


## PART 2

def part_2(instructions):
    waypoint_horizontal_value = 10
    waypoint_vertical_value = 1

    ship_horizontal_value = 0
    ship_vertical_value = 0

    for instruction in instructions:
        command = instruction[0]
        amount = int(instruction[1:])

        # handle waypoint moves
        if command == "N":
            waypoint_vertical_value += amount
        elif command == "S":
            waypoint_vertical_value -= amount
        elif command == "E":
            waypoint_horizontal_value += amount
        elif command == "W":
            waypoint_horizontal_value -= amount

        # handle waypoint rotations
        elif command == "R":
            num_changes = int((amount / 360) * 4)

            for i in range(num_changes):
                (waypoint_horizontal_value, waypoint_vertical_value) = (waypoint_vertical_value, waypoint_horizontal_value)
                waypoint_vertical_value *= -1
            
        elif command == "L":
            num_changes = int((amount / 360) * 4)

            for i in range(num_changes):
                (waypoint_horizontal_value, waypoint_vertical_value) = (waypoint_vertical_value, waypoint_horizontal_value)
                waypoint_horizontal_value *= -1

        # handle ship movement
        elif command == "F":
            ship_horizontal_value += waypoint_horizontal_value * amount
            ship_vertical_value += waypoint_vertical_value * amount

    return abs(ship_horizontal_value) + abs(ship_vertical_value)

print(part_2(rows))
