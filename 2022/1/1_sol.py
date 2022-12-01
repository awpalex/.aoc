def solve_p1(lines):
    elfList = []
    calorieCount = 0
    for line in lines:
        if line.isnumeric():
            calorieCount += int(line)
        else:
            elfList.append(calorieCount)
            calorieCount = 0
    print('Elf',elfList.index(max(elfList))+1,'has the most calories on them. (',max(elfList),')')


def solve_p2(lines):
    elfList = []
    calorieCount = 0
    for line in lines:
        if line.isnumeric():
            calorieCount += int(line)
        else:
            elfList.append(calorieCount)
            calorieCount = 0
    elfList.sort(reverse=True)
    print(sum(elfList[0:3]))

f = open('2022/1/1_input.txt','r')
lines = f.read().splitlines()

solve_p1(lines)
solve_p2(lines)