filename = "C:/Users/Alex/Documents/.aoc/2021/1/1_input.txt"
f = open(filename, "r")
lines = f.read().splitlines()
print(lines)
results = []
sums = []
lastSum = None
numIncreases = 0
window = 3 # for part 1 window=1, for part 2 window = 3

for i in range(0, len(lines)-window+1):
    currentSum = 0
    for j in range(0,window):
        currentSum += int(lines[i+j])
    if lastSum is None:
        results.append("N/A - no previous sum")
    elif lastSum > currentSum:
        results.append("decreased")
    elif lastSum == currentSum:
        results.append("no change")
    elif lastSum < currentSum:
        results.append("increased")
        numIncreases+=1
    sums.append(currentSum)
    lastSum = currentSum

for i in range(0, len(results)):
    print(i,": ",sums[i]," (",results[i],")")
print("number of increases: ",numIncreases)