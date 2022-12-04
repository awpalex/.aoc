def clean_input(input):
    for i in range(len(input)):
        input[i] = input[i].split(',')
        for j in range(len(input[i])):
            input[i][j] = list(map(int,input[i][j].split('-')))
    return input

def solve_p1(input):
    count = 0
    for instruction in input:
        if instruction[0][0] >= instruction[1][0] and instruction[0][1] <= instruction[1][1]:
            count += 1
        elif instruction[1][0] >= instruction[0][0] and instruction[1][1] <= instruction[0][1]:
            count +=1
    print(count)


def solve_p2(input):
    count = 0
    for instruction in input:
        first_nums = set([x for x in range(instruction[0][0], instruction[0][1]+1)])
        second_nums = set([x for x in range(instruction[1][0], instruction[1][1]+1)])
        if set.intersection(first_nums,second_nums) != set():
            count += 1
    print(count)


file = open('2022/4/4_input.txt')
raw_input = file.read().splitlines()

input = clean_input(raw_input)
solve_p1(input)
solve_p2(input)