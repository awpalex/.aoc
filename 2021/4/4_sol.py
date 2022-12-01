def parseInput(filename: str) -> tuple[list, list[list[list[str]]]]:
    f = open(filename).read().splitlines()
    bingoNums = f[0].split(",")
    boards = [[]]
    boardIndex = 0
    for line in f[2:]:
        if line != "":
            boards[boardIndex].append(line.split())
        else:
            boardIndex += 1
            boards.append([])
    return bingoNums, boards


def checkWin(boards: list[list[list[str]]]) -> tuple[int, list]:
    numberOfWinners = 0
    winnerList = set()

    for boardCount, board in enumerate(boards):
        # numberOfWinners += sum(
        #     [
        #         line.count("x") == 5
        #         for line in board
        #     ]
        # )
        # winnerList.add(boardCount)
        for line in board:
            if line.count("x") == len(line):
                winnerList.add(boardCount)
    
        for row in range(0, len(board[0])):
            winningCol = True
            if [board[col][row] for col in range(len(board[0]))].count("x") != 5:
                winningCol = False
            # for col in range(0, len(board[0])):
            #     if board[col][row] != 'x':
            #         winningCol = False
            if winningCol:
                winnerList.add(boardCount)

    return len(winnerList), winnerList


def crossNums(boards: list[list[list[str]]], bingoNum: str) -> list[list[list[str]]]:
    for boardCount, board in enumerate(boards):
        for lineCount, line in enumerate(board):
            for numCount, number in enumerate(line):
                if number == bingoNum:
                    boards[boardCount][lineCount][numCount]= 'x'
    return boards


def solve_p1(bingoNums, boards):
    numberOfWinners = 0
    for bingoNum in bingoNums:
        boards = crossNums(boards, bingoNum)
        numberOfWinners, winnerList = checkWin(boards)
        if numberOfWinners != 0:
            winningNum = bingoNum
            break

    for winner in winnerList:
        print(boards[winner])
        print(winner, 'with number', winningNum)
        noncrossedTotal = 0
        for row in boards[winner]:
            for cell in row:
                if cell != 'x':
                    noncrossedTotal += int(cell)
        print('answer =',int(winningNum)*int(noncrossedTotal))


def solve_p2(bingoNums, boards):
    numberOfBoards = len(boards)
    numberOfWinners = 0
    lastBoardReached = False
    for bingoNum in bingoNums:
        boards = crossNums(boards, bingoNum)
        numberOfWinners, winnerList = checkWin(boards)
        if lastBoardReached and numberOfBoards == numberOfWinners:
            print(boards[loser])
            print(loser, 'with number', bingoNum)
            noncrossedTotal = 0
            for row in boards[loser]:
                for cell in row:
                    if cell != 'x':
                        noncrossedTotal += int(cell)
            print('answer =',int(bingoNum)*int(noncrossedTotal))
            break

        if numberOfWinners == numberOfBoards-1:
            for i in range(0, numberOfBoards):
                if i not in winnerList:
                    loser = i
                    print(loser)
                    lastBoardReached = True


filename = "2021/4/4_input.txt"
bingoNums, boards = parseInput(filename)
solve_p1(bingoNums, boards)
print('------------------------')
solve_p2(bingoNums, boards)
