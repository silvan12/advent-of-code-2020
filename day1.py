lines = open("input.txt").readlines()

numbers = []
for line in lines:
    numbers.append(line.strip('\n'))
# part 1
for number in numbers:
    for plus in numbers:
        if int(number) + int(plus) == 2020:
            print(int(number) * int(plus))
# part 2
for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if int(n1) + int(n2) + int(n3) == 2020:
                print(int(n1) * int(n2) * int(n3))
