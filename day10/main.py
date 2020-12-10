input = open("./day10/input.txt", "r")
rows = []

for line in input:
    rows.append(int(line.strip("\n")))

input.close()

rows.sort()
rows.insert(0, 0) # charging outlet
rows.append(max(*rows) + 3) # built-in adapter

## PART 1

num_1_jolt = 0
num_3_jolt = 0

for i in range(len(rows) - 1):
    diff = rows[i+1] - rows[i]

    if (diff == 1):
        num_1_jolt += 1
    elif (diff == 3):
        num_3_jolt += 1

print("Number of 1 jolt * 3 jolt: " + str(num_1_jolt * num_3_jolt))


## PART 2

num_unique = 0

# recursive approach to counting paths
# spin up recursive call for each possible path to take
# count number of successful paths (e.g. those that reach the finish and are an acceptable jump away) 
def unique_paths_slow(series):
    global num_unique

    if len(series) == 2 and series[1] - series[0] >= 1 and series[1] - series[0] <= 3:
        num_unique += 1
    else:
        for i in range(1, min(4, len(series))):
            diff = series[i] - series[0] >= 1 and series[i] - series[0] <= 3

            if diff:
                unique_paths_slow(series[i:])


# faster approach to counting paths
# the number of ways to reach any given point in the list is
# the sum of the number of ways to reach each number 1-3 below if, if that number is in the seriess
def unique_paths(series):
    path_count = {}

    # initialize with zeroes
    for i in range(-2, max(series) + 1):
        path_count[i] = 0

    # seed 0 with 1 (only one way to get to zero)
    path_count[0] = 1

    # for each number, the # of ways to get to it is the sum of the number of ways to get to each
    # element 1, 2, or 3 behind it, if and only if they are in the series
    for num in series[1:]:
        num_1 = path_count[num-1] if num-1 in series else 0
        num_2 = path_count[num-2] if num-2 in series else 0
        num_3 = path_count[num-3] if num-3 in series else 0

        path_count[num] = num_1 + num_2 + num_3

    return path_count[max(series)]

print("Number of unique paths: " + str(unique_paths(rows)))
