def listToInt(reading: list)-> int:
    value = "".join([str(number) for number in reading])
    value = int(value,2)
    return value

f = open("C:/Users/Alex/Documents/.aoc/2021/3/3_input.txt", "r")
lines = f.read().splitlines()

binaryLength = len(lines[0])

o2Nums = []

for i in range(0,binaryLength):
    for line in lines:
        



"""
find most common bit in pos i
add matching ones to list
repeat

invert to get co2
"""