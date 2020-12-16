from collections import deque

input = open("./day14/input.txt", "r")
rows = []

for line in input:
    rows.append(line.strip("\n"))

input.close()

## PART 1

mask = ""
memory = {}

for row in rows:
    if row.startswith("mask ="):
        mask = row.split(" ")[2]
    else:
        address = int(row[4:].split("]")[0])
        signed_value = int(row.split("= ")[1])
        binary_value = str(bin(signed_value + 2**32)).replace("b1", "000")

        masked_output = ""

        for i in range(len(binary_value)):
            value_to_append = mask[i] if mask[i] != "X" else binary_value[i]
            masked_output += value_to_append

        memory[address] = int(masked_output, 2)

sum = 0

for address in memory:
    sum += memory[address]

print("Sum of values in memory: " + str(sum))

## PART 2

mask = ""
memory = {}

for row in rows:
    if row.startswith("mask ="):
        mask = row.split(" ")[2]
    else:
        address = int(row[4:].split("]")[0])
        value_to_store = int(row.split("= ")[1])
        binary_address = str(bin(address + 2**32)).replace("b1", "000")

        masked_output = ""

        for i in range(len(binary_address)):
            value_to_append = mask[i] if mask[i] != "0" else binary_address[i]
            masked_output += value_to_append

        addresses = []
        queue = deque()
        queue.append(masked_output)

        while len(queue) > 0:
            value = queue.popleft()

            if "X" in value:
                queue.append(value.replace("X", "0", 1))
                queue.append(value.replace("X", "1", 1))
            else:
                addresses.append(value)

        for address in addresses:
            memory[int(address, 2)] = value_to_store

sum = 0

for address in memory:
    sum += memory[address]

print("Sum of values in memory: " + str(sum))