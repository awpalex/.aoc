def listToInt(reading: list)-> int:
    value = "".join([str(number) for number in reading])
    value = int(value,2)
    return value

f = open("C:/Users/Alex/Documents/.aoc/2021/3/3_input.txt", "r")
lines = f.read().splitlines()

binaryLength = len(lines[0])

counter = [0 for x in range(0,binaryLength)]
epsilon = [0 for x in range(0,binaryLength)]
gamma = [0 for x in range(0,binaryLength)]

for line in lines:
    splitLine = [x for x in line]
    for i in range(0,binaryLength):
        if splitLine[i] == "1":
            counter[i] +=1
        else:
            counter[i] -=1
print(counter)

for i in range(0, binaryLength):
    if counter[i] > 0:
        epsilon[i] = 0
        gamma[i] = 1
    elif counter[i] < 0:
        epsilon[i] = 1
        gamma[i] = 0
    else:
        raise Exception("An equal number of 1's and 0's were found in list index",i)
print(epsilon)
print(gamma)

epsilon = listToInt(epsilon)
gamma = listToInt(gamma)

print(epsilon, gamma)

print(epsilon * gamma)