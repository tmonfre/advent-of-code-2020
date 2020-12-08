input = open("./day1/input.txt", "r")
numbers = []

for line in input:
    numbers.append(int(line.strip('\n')))

input.close()

## PART 1

answer = None

for num1 in numbers:
    for num2 in numbers:
        if num1 + num2  == 2020:
            answer = num1 * num2

print("Multiplication answer: " + str(answer))


## PART 2

answer = None

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                answer = num1 * num2 * num3

print("Multiplication answer: " + str(answer))
