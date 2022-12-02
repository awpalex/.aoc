f = open("2022/2/2_input.txt")
input = f.read().splitlines()
winning_games = {
    (1, 2): True,
    (2, 3): True,
    (3, 1): True,
}

def solve_p1():
    my_score = 0
    for game in input:
        game = game.split()
        game[0] = ord(game[0]) - 64
        game[1] = ord(game[1]) - 87
        if tuple(game) in winning_games:
            my_score += 6
        elif game[0] == game[1]:
            my_score += 3
        my_score+=game[1]
    print('1: Your score is',my_score)

def solve_p2():
    my_score = 0
    for game in input:
        game = game.split()
        game[0] = ord(game[0]) - 64
        game[1] = ord(game[1]) - 87
        print('game',game)
        if game[1] == 1:
            print('lose')
            if game[0]-1 != 0:
                my_score+=game[0]-1
            else:
                my_score+=3
        elif game[1] == 2:
            print('draw')
            my_score+=3
            my_score+=game[0]
        elif game[1] == 3:
            print('win')
            my_score+=6
            if game[0]+1 != 4:
                my_score+=game[0]+1
            else:
                my_score+=1
        
    print('2: Your score is',my_score)

solve_p1()
solve_p2()
