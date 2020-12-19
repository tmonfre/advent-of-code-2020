input = open("./day16/input.txt", "r")
rows = [""]
index = 0

for line in input:
    if len(line.strip("\n")) == 0:
        rows.append("")
        index += 1
    else:
        rows[index] += line

input.close()

## PART 1

constraints = []
constraints_str = rows[0].split("\n")
constraints_str.remove('')

for constraint in constraints_str:
    new_const = []

    for val in constraint.split(':')[1].strip(" ").split(' or '):
        split = val.split('-')
        new_const.append([int(split[0]), int(split[1])])
    
    constraints.append(new_const)

nearby_tickets = []

for ticket in rows[2].split('\n')[1:]:
    new_ticket = []

    for num in ticket.split(','):
        new_ticket.append(int(num))

    nearby_tickets.append(new_ticket)


completely_invalid = []

for ticket in nearby_tickets:
    for value in ticket:
        match = False

        for constraint in constraints:
            for constraint_range in constraint:
                match = match or (value in range(constraint_range[0], constraint_range[1] + 1))

        if not match:
            completely_invalid.append(value)

print("Ticket scanning error rate: " + str(sum(completely_invalid)))


## PART 2

tickets_to_evaluate = []

for ticket in nearby_tickets:
    valid_ticket = True

    for value in ticket:
        match = False

        for constraint in constraints:
            for constraint_range in constraint:
                match = match or (value in range(constraint_range[0], constraint_range[1] + 1))

        valid_ticket = valid_ticket and match

    if valid_ticket:
        tickets_to_evaluate.append(ticket)


fields = {}

for rule in rows[0].split('\n')[:-1]:
    rule_name = rule.split(": ")[0]
    rule_constraints = []

    for constraint_str in rule.split(": ")[1].split(" or "):
        rule_constraints.append([int(constraint_str.split('-')[0]), int(constraint_str.split('-')[1])])

    fields[rule_name] = rule_constraints
    
slots_to_determine = list(range(len(fields)))
total_num = len(slots_to_determine)

slots = {}
discovered_rules = []

while len(slots) != total_num:
    for slot in slots_to_determine:
        if slot not in slots:

            matching_rules = []

            for rule in fields:
                if rule not in discovered_rules:
                    match = True
                    
                    for ticket in tickets_to_evaluate:
                        match = match and (
                            ticket[slot] in range(fields[rule][0][0], fields[rule][0][1] + 1) or
                            ticket[slot] in range(fields[rule][1][0], fields[rule][1][1] + 1)
                        )

                    if match:
                        matching_rules.append(rule)

            if len(matching_rules) == 1:
                slots[slot] = matching_rules[0]
                discovered_rules.append(matching_rules[0])


my_ticket = []

for val in rows[1].split('\n')[1].split(','):
    my_ticket.append(int(val))

values_to_evaluate = []

for slot in slots:
    if slots[slot].startswith('departure'):
        values_to_evaluate.append(my_ticket[slot])

answer = 1

for val in values_to_evaluate:
    answer *= val

print("Answer: " + str(answer))