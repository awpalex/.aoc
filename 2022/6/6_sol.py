def find_message(input, len_mark):
    for i in range(len(input)-len_mark-1):
        window = input[i:i+len_mark]
        if len(set(window)) == len(window):
            print(i+len_mark)
            break


f = open('2022/6/6_input.txt')
input = f.read()
find_message(input, 4)
find_message(input, 14)