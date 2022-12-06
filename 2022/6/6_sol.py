f = open('2022/6/6_input.txt')
input = f.read()
print(input)


#input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
for i in range(len(input)-3):
    window = input[i:i+4]
    if len(set(window)) == len(window):
        print(i+4)
        break
    