f = open("2021/2/2_input.txt")
lines = f.read().splitlines()

horPos = 0
depth = 0
for line in lines:
    instruction = line.split(" ")
    if instruction[0] == "forward":
        horPos += int(instruction[1])
    elif instruction[0] == "up":
        depth -= int(instruction[1])
    elif instruction[0] == "down":
        depth += int(instruction[1])
print(horPos * depth)
