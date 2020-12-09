input = open("./day9/input.txt", "r")
rows = []

for line in input:
    rows.append(int(line.strip("\n")))

input.close()

## PART 1

PREAMBLE_LENGTH = 25

first_found_missing = None

for i in range(PREAMBLE_LENGTH, len(rows)):
    current_value = rows[i]
    window = rows[i-PREAMBLE_LENGTH:i]

    found_sum = False

    for other_value in window:
        found_sum = found_sum or (current_value - other_value) in window

    if not found_sum and first_found_missing == None:
        first_found_missing = current_value

print("The first number that doesn't have a window sum is: " + str(first_found_missing))


## PART 2

range_sum = None

for start in range(len(rows)):
    for end in range(len(rows)):
        sub_array = rows[start:end]

        if len(sub_array) > 1:
            sum = 0

            for num in sub_array:
                sum += num

            if sum == first_found_missing and range_sum == None:
                sub_array.sort()
                range_sum = sub_array[0] + sub_array[-1]

print("The sum of the smallest and largest numbers in the contiguous range is: " + str(range_sum))
