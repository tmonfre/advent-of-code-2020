input = open("./day15/input.txt", "r")
rows = []

for line in input:
    rows.append(line.strip("\n"))

input.close()

row = rows[0].split(",")
numbers = []

for value in row:
    numbers.append(int(value))

## PART 1

round_count = 0
last_spoken_number = None
rounds_spoken = {}
spoken_words = []

for starting_number in numbers:
    round_count += 1
    rounds_spoken[starting_number] = [round_count]
    last_spoken_number = starting_number

while round_count < 2020:
    round_count += 1

    if last_spoken_number not in spoken_words or len(rounds_spoken[last_spoken_number]) < 2:
        last_spoken_number = 0

        if 0 not in rounds_spoken:
            rounds_spoken[0] = []

        rounds_spoken[0].insert(0, round_count)
        spoken_words.append(0)

    else:
        last_spoken_number = rounds_spoken[last_spoken_number][0] - rounds_spoken[last_spoken_number][1]

        if last_spoken_number not in rounds_spoken:
            rounds_spoken[last_spoken_number] = []

        rounds_spoken[last_spoken_number].insert(0, round_count)
        spoken_words.append(last_spoken_number)

print("2020th spoken word: " + str(last_spoken_number))


## PART 2

round_count = 0
last_spoken_number = None
rounds_spoken = {}
spoken_words = []

for starting_number in numbers:
    round_count += 1
    rounds_spoken[starting_number] = [round_count]
    last_spoken_number = starting_number

while round_count < 30000000:
    round_count += 1

    if last_spoken_number not in spoken_words or len(rounds_spoken[last_spoken_number]) < 2:
        last_spoken_number = 0

        if 0 not in rounds_spoken:
            rounds_spoken[0] = []

        rounds_spoken[0].insert(0, round_count)
        spoken_words.append(0)

    else:
        last_spoken_number = rounds_spoken[last_spoken_number][0] - rounds_spoken[last_spoken_number][1]

        if last_spoken_number not in rounds_spoken:
            rounds_spoken[last_spoken_number] = []

        rounds_spoken[last_spoken_number].insert(0, round_count)
        spoken_words.append(last_spoken_number)

print("30000000th spoken word: " + str(last_spoken_number))
