MAX_X = 1000
MAX_Y = 1000


def drawLine(board, instruction):

    return board


f = open("2021/5/5_input.txt")
lines = f.read().splitlines()
board = [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]

instructions = []
for line in lines:
    splitLine = line.split()
    instruction = []
    coordX = splitLine[0].split(",")
    coordY = splitLine[-1].split(",")
    instruction.append(coordX)
    instruction.append(coordY)
    instructions.append(instruction)

# remove not straight lines
for instruction in instructions:
    if instruction[0][0] != instruction[1][0] or instruction[1][0] != instruction[1][1]:
        instructions.pop(instructions.index(instruction))
for instruction in instructions:
    board = drawLine(board, instruction)
