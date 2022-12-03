def get_priority(letter: str) -> int:
    priority = ord(letter)
    if priority >= 97 :
        priority -= 96
    else:
        priority -= 38
    return priority


def solve_p1(input):
    shared_letter_priority = []
    for line in input:
        line_length = len(line)
        first_comp = line[0:line_length//2]
        second_comp = line[line_length//2:]
        for letter in first_comp:
            if letter in second_comp:
                priority = get_priority(letter)
                shared_letter_priority.append(priority)
                break
    print(sum(shared_letter_priority))


def solve_p2(input):
    priorities = []
    counter = 0
    while counter < (len(input))-2:
        print(counter, len(input))
        first_bag = set(input[counter])
        second_bag = set(input[counter+1])
        third_bag = set(input[counter+2])
        common_letters = first_bag & second_bag & third_bag
        for letter in common_letters:
            priorities.append(get_priority(letter))
        counter += 3
    print(sum(priorities))


f = open('2022/3/3_input.txt')
input = f.read().splitlines()
solve_p1(input)
solve_p2(input)