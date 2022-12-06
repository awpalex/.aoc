import copy

def move_crate_9000(from_index,to_index):
    crate = board[from_index].pop()
    board[to_index].append(crate)


def move_crate_9001(num_crates,from_index,to_index):
    crates = board_original[from_index][-num_crates:]
    board_original[from_index] = board_original[from_index][0:-num_crates]
    for crate in crates:
        board_original[to_index].append(crate)


f = open('2022/5/5_input.txt')
input = f.read().splitlines()

characters = []
board_original = []
for line in input:
    if '[' not in line:
        break
    index=0
    for char in line:
        if char.isalnum():
            characters.append([char,index//4])
        index += 1
    
characters.reverse()
max = 0
for entry in characters:
    if entry[1] > max:
        max = entry[1]
board_original = []
for i in range(max+1):
    board_original.append([])
for entry in characters:
    board_original[entry[1]].append(entry[0])

# lukes code
# for line in input:
#     if '[' not in line:
#         break
#     for i, c in enumerate(line[1::4]):
#         if not c.isalnum():
#             continue
#         if i >= len(board_original):
#             board_original += [[] for _ in range(1 + i - len(board_original))]
#         board_original[i].append(c)
        
# for row in board_original:
#     row.reverse()

board = copy.deepcopy(board_original)

for line in input:
    if 'move' in line:
        line = line.split()
        instruction = [int(char) for char in line if char.isnumeric()]
        for i in range(instruction[0]):
            move_crate_9000(instruction[1]-1,instruction[2]-1)
        move_crate_9001(instruction[0],instruction[1]-1,instruction[2]-1)
        
a=''
b=''
for line in board:
    a = a+(line[-1])
for line in board_original:
    b = b+(line[-1])
print('p1:',a)
print('p2:',b)
