input = open("./day8/input.txt", "r")
rows = []

for line in input:
    rows.append(line.strip("\n"))

input.close()

## PART 1

visited_lines = set()
found_double_visit = False

index = 0
accumulator = 0

while not found_double_visit:
    if index in visited_lines:
        found_double_visit = True
    else:
        visited_lines.add(index)

        line = rows[index]
        instruction = line.split(" ")[0]
        amount = int(line.split(" ")[1])

        if instruction == "acc":
            accumulator += amount
            index += 1
        elif instruction == "jmp":
            index += amount
        elif instruction == "nop":
            index += 1

print("Value in the accumulator: " + str(accumulator))


## PART 2

jmp_indexes = []
nop_indexes = []

for i in range(len(rows)):
    instruction = rows[i].split(" ")[0]
    
    if (instruction == "jmp"):
        jmp_indexes.append(i)
    elif (instruction == "nop"):
        nop_indexes.append(i)

found_with_jmp = False

for jmp_change_index in jmp_indexes:
    visited_lines = set()
    found_double_visit = False
    index = 0
    accumulator = 0

    while not found_double_visit and index < len(rows):
        if index in visited_lines:
            found_double_visit = True
        else:
            visited_lines.add(index)

            line = rows[index]
            instruction = line.split(" ")[0]
            amount = int(line.split(" ")[1])

            if (index == jmp_change_index and instruction == "jmp"):
                instruction = "nop"

            if instruction == "acc":
                accumulator += amount
                index += 1
            elif instruction == "jmp":
                index += amount
            elif instruction == "nop":
                index += 1

    if not found_double_visit:
        print("Value in the accumulator after the program terminates: " + str(accumulator))
        found_with_jmp = True

if (not found_with_jmp):
    for nop_change_index in nop_indexes:
        visited_lines = set()
        found_double_visit = False
        index = 0
        accumulator = 0

        while not found_double_visit and index < len(rows):
            if index in visited_lines:
                found_double_visit = True
            else:
                visited_lines.add(index)

                line = rows[index]
                instruction = line.split(" ")[0]
                amount = int(line.split(" ")[1])

                if (index == nop_change_index and instruction == "nop"):
                    instruction = "jmp"

                if instruction == "acc":
                    accumulator += amount
                    index += 1
                elif instruction == "jmp":
                    index += amount
                elif instruction == "nop":
                    index += 1

        if not found_double_visit:
            print("Value in the accumulator after the program terminates: " + str(accumulator))
