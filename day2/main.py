input = open("./day2/input.txt", "r")
separations = []

for line in input:
    separations.append(line.split(' '))

input.close()

## PART 1

valid_count = 0

for input_separation in separations:
    min_occurrence = int(input_separation[0].split('-')[0])
    max_occurrence = int(input_separation[0].split('-')[1])
    character = input_separation[1][0]
    password = input_separation[2].strip('\n')

    num_times_in_password = password.count(character)

    if num_times_in_password >= min_occurrence and num_times_in_password <= max_occurrence:
        valid_count += 1

print("Number of valid passwords: " + str(valid_count))


## PART 2

valid_count = 0

for input_separation in separations:
    first_index = int(input_separation[0].split('-')[0]) - 1
    second_index = int(input_separation[0].split('-')[1]) - 1
    character = input_separation[1][0]
    password = input_separation[2].strip('\n')

    match_count = (password[first_index] == character) + (password[second_index] == character)

    if (match_count == 1):
        valid_count += 1

print("Number of valid passwords: " + str(valid_count))
