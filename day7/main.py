from collections import deque
from typing import Deque

input = open("./day7/input.txt", "r")
rows = []

for line in input:
    rows.append(line.strip("\n"))

input.close()

## PART 1

bags = {}

for row in rows:
    split = row.split("contain")
    bag_type = split[0].strip()

    carry_list_raw = split[1].strip('.').split(",")
    carry_list = []

    for item in carry_list_raw:
        item = item if item.endswith('s') else item + 's'
        carry_list.append(" ".join(item.strip().split(" ")[1:]))

    bags[bag_type] = carry_list


valid_holders = []

queue = Deque()

queue.append("shiny gold bags")

while len(queue) > 0:
    search_term = queue.popleft()

    for bag_type in bags:
        if search_term in bags[bag_type] and bag_type not in valid_holders:
            # print("APPENDING " + bag_type, "was looking for: " + search_term)
            queue.append(bag_type)
            valid_holders.append(bag_type)
    
print("Number of bag types that can hold shiny gold bags: " + str(len(valid_holders)))


## PART 2

bags = {}

for row in rows:
    split = row.split("contain")
    bag_type = split[0].strip()

    carry_list_raw = split[1].strip('.').split(",")
    carry_list = {}

    for item in carry_list_raw:
        if "no other bags" in item:
            continue

        item = (item if item.endswith('s') else item + 's').strip(" ").strip("\n")

        item_amount = int(item.split(' ')[0])
        item_name = " ".join(item.split(' ')[1:])

        carry_list[item_name] = item_amount

    bags[bag_type] = carry_list


sum = 0
queue = deque()

queue.append("shiny gold bags")

while len(queue) > 0:
    search_term = queue.popleft()

    for bag in bags[search_term]:
        sum += bags[search_term][bag]

        for i in range(bags[search_term][bag]):
            queue.append(bag)

print("Total number of bags: " + str(sum))