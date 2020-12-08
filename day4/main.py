import re

input = open("./day4/input.txt", "r")
rows = []

for line in input:
    rows.append(line)

input.close()

for i in range(len(rows)):
    rows[i] = rows[i].strip("\n")

passports = [""]
index = 0

for row in rows:
    if len(row) > 0:
        passports[index] += row if len(passports[index]) == 0 else " " + row
    else:
        index += 1
        passports.append("")

passport_objects = []

for passport in passports:
    passport_input = passport.split(" ")
    passport_values = {}

    for input in passport_input:
        passport_values[input.split(":")[0]] = input.split(":")[1]

    passport_objects.append(passport_values)

passports = passport_objects


## PART 1

valid_count = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passport in passports:
    is_valid = True

    for field in required_fields:
        try:
            is_valid = is_valid and passport[field] != None
        except KeyError:
            is_valid = False

    valid_count += is_valid

print("Number of valid passports: " + str(valid_count))


## PART 2

valid_count = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = []

for passport in passports:
    is_valid = True

    for field in required_fields:
        try:
            is_valid = is_valid and passport[field] != None
        except KeyError:
            is_valid = False

    if is_valid:
        valid_passports.append(passport)

for passport in passports:
    is_valid = True

    try:
        is_valid = is_valid and len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002
        is_valid = is_valid and len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020
        is_valid = is_valid and len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030

        if "in" in passport['hgt']:
            is_valid = is_valid and int(passport['hgt'].split("in")[0]) >= 59 and int(passport['hgt'].split("in")[0]) <= 76
        elif "cm" in passport['hgt']:
            is_valid = is_valid and int(passport['hgt'].split("cm")[0]) >= 150 and int(passport['hgt'].split("cm")[0]) <= 193
        else:
            is_valid = False

        is_valid = is_valid and re.match("^\#[a-f0-9]{6}$$", passport['hcl']) != None
        is_valid = is_valid and passport['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        is_valid = is_valid and len(passport['pid']) == 9 and int(passport['pid']) >= 0


    except KeyError:
        is_valid = False

    valid_count += is_valid

print("Number of valid passports: " + str(valid_count))
